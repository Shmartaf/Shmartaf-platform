import random
from uuid import uuid4

from faker import Faker
from sqlalchemy.exc import IntegrityError

from backend.database import schemas
from backend.database.dal import DataAccessLayer
from backend.database.models import (
    Babysitter,
    BabysitterSkill,
    Children,
    ChildrensNeeds,
    Favorite,
    Parent,
    ParentsChildrens,
    Review,
    SpecialNeed,
    SpecialSkill,
    User,
)

fake = Faker()
dal = DataAccessLayer()


def retry_on_duplicate(func):
    """Decorator to retry a function with a new ID if an IntegrityError is caught due to duplication."""

    def wrapper(*args, **kwargs):
        max_attempts = 5
        for _ in range(max_attempts):
            try:
                return func(*args, **kwargs)
            except IntegrityError:
                print("Duplicate entry detected, retrying with a new ID...")
                if "id" in kwargs:
                    kwargs["id"] = uuid4()
                else:
                    args = list(args)
                    if args:
                        args[0] = uuid4()  # Assuming the first argument is the ID for simplicity
        raise Exception("Failed to create a unique entity after several attempts.")

    return wrapper


@retry_on_duplicate
def create_skill():
    skill_schema = schemas.CertificationSchema(id=uuid4(), skillname=fake.word())
    return dal.create(model=SpecialSkill, schema=skill_schema)


@retry_on_duplicate
def create_need():
    need_schema = schemas.RequirementsSchema(id=uuid4(), needname=fake.word())
    return dal.create(model=SpecialNeed, schema=need_schema)


@retry_on_duplicate
def create_user():
    user_schema = schemas.UserSchema(
        id=uuid4(),
        name=fake.name(),
        password=fake.password(),
        email=fake.email(),
        phone=fake.phone_number(),
        registrationdate=fake.date_of_birth(),
        city=fake.city(),
        street=fake.street_name(),
    )
    return dal.create(model=User, schema=user_schema)


def create_babysitter(user_id):
    babysitter_schema = schemas.BabysitterRequestSchema(
        id=user_id,  # Assuming this should be a separate unique identifier, not the user_id
        pictureid=random.randint(1, 10),
        description=fake.text(),
    )
    return dal.create(model=Babysitter, schema=babysitter_schema)


def create_parent(user_id):
    parent_schema = schemas.ParentSchema(
        id=user_id,  # Assuming this should be a separate unique identifier, not the user_id
        description=fake.text(),
    )
    return dal.create(model=Parent, schema=parent_schema)


# @retry_on_duplicate
def create_children(parent_id):
    children_schema = schemas.ChildrenRequestSchema(
        id=uuid4(),
        name=fake.name(),
        birthdate=fake.date_of_birth(),
        gender=random.choice(["M", "F"]),
    )
    dal.create(model=Children, schema=children_schema)
    parent_children_schema = schemas.ParentChildrenRequestSchema(parentid=parent_id, childid=children_schema.id)
    return dal.create(model=ParentsChildrens, schema=parent_children_schema)  # Adjust DAL method signature as needed


# @retry_on_duplicate
def create_children_requirements(child_id, need_id):
    children_requirements_schema = schemas.ChildReqirmentsRequestSchema(
        childid=child_id,
        needid=need_id,
        needrank=random.randint(1, 5),
    )
    return dal.create(model=ChildrensNeeds, schema=children_requirements_schema)


def mock_db(n):
    skills = []
    needs = []
    # users = []
    for _ in range(20):
        skill = create_skill()
        skills.append(skill)
        need = create_need()
        needs.append(need)

    # Create users, parents/babysitters, and children with needs
    for _ in range(n):
        user = create_user()
        if random.choice([True, False]):  # Randomly decide between parent and babysitter
            parent = create_parent(user.id)
            for _ in range(random.randint(1, 3)):  # Each parent can have 1-3 children
                child = create_children(parent.id)
                for need in random.sample(
                    needs, random.randint(1, min(3, len(needs)))
                ):  # Assign 1-3 needs to each child
                    create_children_requirements(child.childid, need.id)
        else:
            babysitter = create_babysitter(user.id)
            random_skills = random.sample(skills, random.randint(1, min(5, len(skills))))
            for skill in random_skills:
                babysitter_skill_schema = schemas.BabysitterCerticationRequestSchema(
                    babysitterid=babysitter.id,
                    id=skill.id,
                    skillrank=random.randint(1, 5),
                )
                dal.create(model=BabysitterSkill, schema=babysitter_skill_schema)

    for _ in range(n):
        parent = random.choice(dal.get_all(model=Parent))
        babysitter = random.choice(dal.get_all(model=Babysitter))
        favorite_schema = schemas.FavoriteRequestSchema(parentid=parent.id, babysitterid=babysitter.id)
        try:
            dal.create(model=Favorite, schema=favorite_schema)
        except IntegrityError:
            print("Duplicate favorite entry detected, skipping...")
            pass
        review_schema = schemas.ReviewSchema(
            id=uuid4(),
            reviewerid=parent.id,
            reviewedid=babysitter.id,
            rating=random.randint(1, 5),
            comment=fake.text(),
            flexibilityrating=random.randint(1, 5),
            reliabilityrating=random.randint(1, 5),
            interpersonalrating=random.randint(1, 5),
            registrationdate=fake.date_of_birth(),
        )
        dal.create(model=Review, schema=review_schema)

    print("Database mock data generation complete.")


mock_db(3)
pass

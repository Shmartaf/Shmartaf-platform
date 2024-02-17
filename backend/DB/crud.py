import models
import schemas
from sqlalchemy.orm import Session, joinedload

# USER


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.userid == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.User):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# BABYSITTER


def get_babysitter(db: Session, babysitter_id: int):
    return db.query(models.Babysitter).filter(models.Babysitter.babysitterid == babysitter_id).first()


def get_babysitters(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Babysitter).offset(skip).limit(limit).all()


def create_babysitter(db: Session, babysitter: schemas.Babysitter):
    db_babysitter = models.Babysitter(**babysitter.dict())
    db.add(db_babysitter)
    db.commit()
    db.refresh(db_babysitter)
    return db_babysitter


# PARENT


def get_parent(db: Session, parent_id: int):
    return db.query(models.Parent).filter(models.Parent.parentid == parent_id).first()


def get_parent_with_user(db: Session, parent_id: int):
    return (
        db.query(models.Parent)
        .options(joinedload(models.Parent.user))
        .filter(models.Parent.parentid == parent_id)
        .first(),
    )


def get_parents(db: Session, skip: int = 0, limit: int = 100):
    return (
        db.query(models.Parent)
        .join(models.User, models.User.userid == models.Parent.parentid)
        .offset(skip)
        .limit(limit)
        .all()
    )


def create_parent(db: Session, parent: schemas.Parent):
    db_parent = models.Parent(**parent.dict())
    db.add(db_parent)
    db.commit()
    db.refresh(db_parent)
    return db_parent


# CHILDREN


def get_children(db: Session, child_id: int):
    return db.query(models.Children).filter(models.Children.childid == child_id).first()


def get_childrens(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Children).offset(skip).limit(limit).all()


def create_children(db: Session, children: schemas.Children):
    db_children = models.Children(**children.dict())
    db.add(db_children)
    db.commit()
    db.refresh(db_children)
    return db_children


# PARENTS_CHILDRENS


def get_all_parents_childrens(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.ParentsChildrens).offset(skip).limit(limit).all()


def get_parents_childrens(db: Session, parent_id: int, child_id: int):
    # Preform join between parents_childrens and children and parent
    return (
        db.query(models.ParentsChildrens)
        .join(models.Children, models.Children.childid == models.ParentsChildrens.childid)
        .join(models.Parent, models.Parent.parentid == models.ParentsChildrens.parentid)
        .filter(models.ParentsChildrens.parentid == parent_id)
        .filter(models.ParentsChildrens.childid == child_id)
        .first()
    )


def get_parents_childrens_by_parent(db: Session, parent_id: int):
    return (
        db.query(models.ParentsChildrens)
        .join(models.Children, models.Children.childid == models.ParentsChildrens.childid)
        .join(models.Parent, models.Parent.parentid == models.ParentsChildrens.parentid)
        .filter(models.ParentsChildrens.parentid == parent_id)
        .all()
    )


def get_parents_childrens_by_child(db: Session, child_id: int):
    return (
        db.query(models.ParentsChildrens)
        .join(models.Children, models.Children.childid == models.ParentsChildrens.childid)
        .join(models.Parent, models.Parent.parentid == models.ParentsChildrens.parentid)
        .filter(models.ParentsChildrens.childid == child_id)
        .all()
    )


def create_parents_childrens(db: Session, parents_childrens: schemas.ParentsChildrens):
    db_parents_childrens = models.ParentsChildrens(**parents_childrens.dict())
    db.add(db_parents_childrens)
    db.commit()
    db.refresh(db_parents_childrens)
    return db_parents_childrens


def delete_parents_childrens(db: Session, parent_id: int, child_id: int):
    db.query(models.ParentsChildrens).filter(models.ParentsChildrens.parentid == parent_id).filter(
        models.ParentsChildrens.childid == child_id
    ).delete()
    db.commit()
    return {"message": "ParentsChildrens deleted successfully"}


def delete_parents_childrens_by_parent(db: Session, parent_id: int):
    db.query(models.ParentsChildrens).filter(models.ParentsChildrens.parentid == parent_id).delete()
    db.commit()
    return {"message": "ParentsChildrens deleted successfully"}


def delete_parents_childrens_by_child(db: Session, child_id: int):
    db.query(models.ParentsChildrens).filter(models.ParentsChildrens.childid == child_id).delete()
    db.commit()
    return {"message": "ParentsChildrens deleted successfully"}


# REVIEW


def get_review_with_user_and_babysitter(db: Session, review_id: int):
    return (
        db.query(models.Review)
        .join(models.User, models.User.id == models.Review.reviewer_id)
        .join(models.Babysitter, models.Babysitter.id == models.Review.reviewed_id)
        .filter(models.Review.review_id == review_id)
        .first()
    )


def get_reviews_with_user_and_babysitter(db: Session, skip: int = 0, limit: int = 100):
    return (
        db.query(models.Review)
        .join(models.User, models.User.id == models.Review.reviewer_id)
        .join(models.Babysitter, models.Babysitter.id == models.Review.reviewed_id)
        .offset(skip)
        .limit(limit)
        .all()
    )


def create_review_with_user_and_babysitter(db: Session, review: schemas.Review):
    db_review = models.Review(**review.dict())
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review


def get_review_by_reviewer_with_user_and_babysitter(db: Session, reviewer_id: int):
    return (
        db.query(models.Review)
        .join(models.User, models.User.id == models.Review.reviewer_id)
        .join(models.Babysitter, models.Babysitter.id == models.Review.reviewed_id)
        .filter(models.Review.reviewer_id == reviewer_id)
        .all()
    )


def get_review_by_reviewed_with_user_and_babysitter(db: Session, reviewed_id: int):
    return (
        db.query(models.Review)
        .join(models.User, models.User.id == models.Review.reviewer_id)
        .join(models.Babysitter, models.Babysitter.id == models.Review.reviewed_id)
        .filter(models.Review.reviewed_id == reviewed_id)
        .all()
    )


def delete_review_with_user_and_babysitter(db: Session, review_id: int):
    db.query(models.Review).filter(models.Review.review_id == review_id).delete()
    db.commit()
    return {"message": "Review deleted successfully"}


def delete_review_by_reviewer_with_user_and_babysitter(db: Session, reviewer_id: int):
    db.query(models.Review).filter(models.Review.reviewer_id == reviewer_id).delete()
    db.commit()
    return {"message": "Review deleted successfully"}


def delete_review_by_reviewed_with_user_and_babysitter(db: Session, reviewed_id: int):
    db.query(models.Review).filter(models.Review.reviewed_id == reviewed_id).delete()
    db.commit()
    return {"message": "Review deleted successfully"}


# SPECIALNEED


def get_specialneed(db: Session, need_id: int):
    return db.query(models.SpecialNeed).filter(models.SpecialNeed.needid == need_id).first()


def get_specialneeds(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.SpecialNeed).offset(skip).limit(limit).all()


def create_specialneed(db: Session, specialneed: schemas.SpecialNeed):
    db_specialneed = models.SpecialNeed(**specialneed.dict())
    db.add(db_specialneed)
    db.commit()
    db.refresh(db_specialneed)
    return db_specialneed


# SPECIALSKILL


def get_specialskill(db: Session, skill_id: int):
    return db.query(models.SpecialSkill).filter(models.SpecialSkill.skillid == skill_id).first()


def get_specialskills(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.SpecialSkill).offset(skip).limit(limit).all()


def create_specialskill(db: Session, specialskill: schemas.SpecialSkill):
    db_specialskill = models.SpecialSkill(**specialskill.dict())
    db.add(db_specialskill)
    db.commit()
    db.refresh(db_specialskill)
    return db_specialskill


# BABYSITTERSKILL


def get_all_skills(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.BabysitterSkill).offset(skip).limit(limit).all()


# all babysitter with skill
def get_babysitters_with_skill(db: Session, skill_id: int, skip: int = 0, limit: int = 100):
    return (
        db.query(models.BabysitterSkill)
        .join(models.Babysitter)  # Perform join with the Babysitter table
        .join(models.SpecialSkill)  # Perform join with the SpecialSkill table
        .filter(models.BabysitterSkill.skillid == skill_id)
        .offset(skip)
        .limit(limit)
        .all()
    )


# all skills of a babysitter
def get_babysitterskills_with_user(db: Session, babysitter_id: int, skip: int = 0, limit: int = 100):
    return (
        db.query(models.BabysitterSkill)
        .join(models.Babysitter)  # Perform join with the Babysitter table
        .join(models.User)  # Perform join with the User table
        .filter(models.BabysitterSkill.babysitterid == babysitter_id)
        .offset(skip)
        .limit(limit)
        .all()
    )


def create_babysitterskill(db: Session, babysitterskill: schemas.BabysitterSkill):
    db_babysitterskill = models.BabysitterSkill(**babysitterskill.dict())
    db.add(db_babysitterskill)
    db.commit()
    db.refresh(db_babysitterskill)
    return db_babysitterskill


# NEEDSKILL


def get_needskill(db: Session, need_id: int, skill_id: int):
    return (
        db.query(models.NeedSkill)
        .join(models.SpecialNeed)  # Perform join with the SpecialNeed table
        .join(models.SpecialSkill)  # Perform join with the SpecialSkill table
        .filter(models.NeedSkill.needid == need_id)
        .filter(models.NeedSkill.skillid == skill_id)
        .first()
    )


def get_needskills_with_specialneed(db: Session, need_id: int, skip: int = 0, limit: int = 100):
    return (
        db.query(models.NeedSkill)
        .join(models.SpecialNeed)  # Perform join with the SpecialNeed table
        .join(models.SpecialSkill)  # Perform join with the SpecialSkill table
        .filter(models.NeedSkill.needid == need_id)
        .offset(skip)
        .limit(limit)
        .all()
    )


def get_needskills_with_specialskill(db: Session, skill_id: int, skip: int = 0, limit: int = 100):
    return (
        db.query(models.NeedSkill)
        .join(models.SpecialNeed)  # Perform join with the SpecialNeed table
        .join(models.SpecialSkill)  # Perform join with the SpecialSkill table
        .filter(models.NeedSkill.skillid == skill_id)
        .offset(skip)
        .limit(limit)
        .all()
    )


def create_needskill(db: Session, needskill: schemas.NeedSkill):
    db_needskill = models.NeedSkill(**needskill.dict())
    db.add(db_needskill)
    db.commit()
    db.refresh(db_needskill)
    return db_needskill


# FAVORITE


def get_favorite(db: Session, parent_id: int, babysitter_id: int):
    return (
        db.query(models.Favorite)
        .join(models.Parent)  # Perform join with the Parent table
        .join(models.Babysitter)  # Perform join with the Babysitter table
        .filter(models.Favorite.parentid == parent_id)
        .filter(models.Favorite.babysitterid == babysitter_id)
        .first()
    )


def get_favorites_with_parent(db: Session, parent_id: int, skip: int = 0, limit: int = 100):
    return (
        db.query(models.Favorite)
        .join(models.Parent)  # Perform join with the Parent table
        .join(models.Babysitter)  # Perform join with the Babysitter table
        .filter(models.Favorite.parentid == parent_id)
        .offset(skip)
        .limit(limit)
        .all()
    )


def get_favorites_with_babysitter(db: Session, babysitter_id: int, skip: int = 0, limit: int = 100):
    return (
        db.query(models.Favorite)
        .join(models.Parent)  # Perform join with the Parent table
        .join(models.Babysitter)  # Perform join with the Babysitter table
        .filter(models.Favorite.babysitterid == babysitter_id)
        .offset(skip)
        .limit(limit)
        .all()
    )


def create_favorite(db: Session, favorite: schemas.Favorite):
    db_favorite = models.Favorite(**favorite.dict())
    db.add(db_favorite)
    db.commit()
    db.refresh(db_favorite)
    return db_favorite


def delete_favorite(db: Session, parent_id: int, babysitter_id: int):
    db.query(models.Favorite).filter(models.Favorite.parentid == parent_id).filter(
        models.Favorite.babysitterid == babysitter_id
    ).delete()
    db.commit()
    return {"message": "Favorite deleted successfully"}


def delete_favorite_by_parent(db: Session, parent_id: int):
    db.query(models.Favorite).filter(models.Favorite.parentid == parent_id).delete()
    db.commit()
    return {"message": "Favorite deleted successfully"}


def delete_favorite_by_babysitter(db: Session, babysitter_id: int):
    db.query(models.Favorite).filter(models.Favorite.babysitterid == babysitter_id).delete()
    db.commit()
    return {"message": "Favorite deleted successfully"}


# CONTACTED


def get_all_contacted(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Contacted).offset(skip).limit(limit).all()


def get_contacted(db: Session, contact_id: int):
    return db.query(models.Contacted).filter(models.Contacted.contactid == contact_id).first()


def get_contacteds_with_parent(db: Session, parent_id: int, skip: int = 0, limit: int = 100):
    return (
        db.query(models.Contacted)
        .join(models.Parent)  # Perform join with the Parent table
        .join(models.Babysitter)  # Perform join with the Babysitter table
        .filter(models.Contacted.parentid == parent_id)
        .offset(skip)
        .limit(limit)
        .all()
    )


def get_contacteds_with_babysitter(db: Session, babysitter_id: int, skip: int = 0, limit: int = 100):
    return (
        db.query(models.Contacted)
        .join(models.Parent)  # Perform join with the Parent table
        .join(models.Babysitter)  # Perform join with the Babysitter table
        .filter(models.Contacted.babysitterid == babysitter_id)
        .offset(skip)
        .limit(limit)
        .all()
    )


def create_contacted(db: Session, contacted: schemas.Contacted):
    db_contacted = models.Contacted(**contacted.dict())
    db.add(db_contacted)
    db.commit()
    db.refresh(db_contacted)
    return db_contacted


def delete_contacted(db: Session, contact_id: int):
    db.query(models.Contacted).filter(models.Contacted.contactid == contact_id).delete()
    db.commit()
    return {"message": "Contacted deleted successfully"}


# SCHEDULER


def get_scheduler(db: Session, scheduler_id: int):
    return db.query(models.Scheduler).filter(models.Scheduler.babysitterid == scheduler_id).first()


def get_schedulers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Scheduler).offset(skip).limit(limit).all()


def create_scheduler(db: Session, scheduler: schemas.Scheduler):
    db_scheduler = models.Scheduler(**scheduler.dict())
    db.add(db_scheduler)
    db.commit()
    db.refresh(db_scheduler)
    return db_scheduler


def delete_scheduler(db: Session, scheduler_id: int):
    db.query(models.Scheduler).filter(models.Scheduler.babysitterid == scheduler_id).delete()
    db.commit()
    return {"message": "Scheduler deleted successfully"}

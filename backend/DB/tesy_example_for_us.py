import crud
from database import SessionLocal

db = SessionLocal()


res = crud.get_babysitters(db, skip=0, limit=10)
for babysitter in res:
    skills = babysitter.skills
# pass


# for user, babysitter in res:
#     print(Users.name, Babysitter.description)

# # Example usage of creating records
# try:
#     # Create a user record
#     user = Users(
#         userid="1",
#         name="or",
#         email="or@test.com",
#         password="1234",
#         registrationdate="2021-01-01",
#         city="tel aviv",
#         street="rothschild",
#         phone="1234567",
#     )
#     db.create(user)

#     # Create a babysitter record
#     babysitter = Babysitter(babysitterid=1, pictureid=1, description="I am a babysitter")
#     db.create(babysitter)

#     # Create a parent record
#     parent = Parent(parentid=1, description="I am a parent")
#     db.create(parent)

#     # Create a special skill record
#     special_skill = SpecialSkill(skillid=1, skillname="I am a special skill")
#     db.create(special_skill)

#     # Create a favorite record
#     favorite = Favorite(parentid=1, babysitterid=1)
#     db.create(favorite)

#     # Create a review record
#     review = Reviews(reviewid=1, reviewerid=1, reviewedid=1, rating=5, comment="I am a review")
#     db.create(review)

#     # Create a babysitter skill record
#     babysitter_skill = BabysitterSkill(skillid=1, babysitterid=1, skillrank=1)
#     db.create(babysitter_skill)

#     # Create a child record
#     child = Children(childid=1, name="or", birthdate=datetime.now(), gender="male")
#     db.create(child)

#     # Create a special need record
#     special_need = SpecialNeed(needid=1, needname="I am a special need")
#     db.create(special_need)

#     # Create a scheduler record
#     scheduler = Scheduler(babysitterid=1, dayinweek=1, starttime="08:00", endtime="12:00")
#     db.create(scheduler)

#     # Create a contacted record
#     contacted = Contacted(contactid=1, babysitterid=1, parentid=1, date="2021-01-01")
#     db.create(contacted)

#     # Add your test code here

# except Exception as e:
#     # Handle the exception
#     print("Test failed:", str(e))
#     # Delete the created records in reverse order
#     # db.delete(child)
#     db.delete(scheduler)
#     db.delete(babysitter_skill)
#     db.delete(review)
#     db.delete(favorite)
#     db.delete(special_skill)
#     db.delete(parent)
#     db.delete(babysitter)
#     db.delete(user)

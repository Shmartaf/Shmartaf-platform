import crud
import pandas as pd
from database import SessionLocal
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

db = SessionLocal()

# Fetch data using CRUD operations
skills = crud.get_specialskills(db)
babysitters = crud.get_babysitters(db)

children_needs = crud.get_specialneeds(db)
parents_childrens = crud.get_parents(db)

results = []
for babysitter in babysitters:
    for skill in babysitter.skills:
        for need in children_needs:
            for need_skill in need.need_skills:
                if need_skill.skillid == skill.skillid:
                    for parent_child in parents_childrens:
                        for children in parent_child.children:
                            for childneed in children.needs_association:
                                if childneed.needid == need_skill.needid:
                                    results.append(
                                        {
                                            "babysitter_id": skill.babysitterid,
                                            "parent_id": parent_child.parentid,
                                            "skill_name": skill.skill.skillname,
                                            "need_name": need.needname,
                                        }
                                    )

print(results)

# המרת התוצאות ל-DataFrame
df = pd.DataFrame(results)

# יצירת תכונות בינאריות
# for skill in all_skills:
#   df[f"skill_{skill}"] = df['skill_name'].apply(lambda x: 1 if x == skill else 0)

# for need in all_needs:
#  df[f"need_{need}"] = df['need_name'].apply(lambda x: 1 if x == need else 0)

contacted_records = crud.get_all_contacted(db)
# הנחה שלכל רשומה יש מאפיינים parentid ו babysitterid
contacted_pairs = {(record.parentid, record.babysitterid) for record in contacted_records}
# נניח שיש לנו עמודות parentid ו babysitterid ב-DataFrame שלנו
df["contacted"] = df.apply(lambda row: 1 if (row["parent_id"], row["babysitter_id"]) in contacted_pairs else 0, axis=1)

# Assuming 'df' is your DataFrame after fetching the results
# Convert 'skill_name' and 'need_name' to a one-hot encoded format
df_skills_needs = pd.get_dummies(df[["skill_name", "need_name"]])

# Include the 'babysitter_id' and 'parent_id' in the DataFrame if you plan to use them as features
# Otherwise, ensure they are not included in the features DataFrame if they are only identifiers
df_final = pd.concat([df_skills_needs, df["contacted"]], axis=1)

# Now 'df_final' is ready for machine learning models

# Splitting the data for training and testing
X = df_final.drop("contacted", axis=1)  # Features
y = df_final["contacted"]  # Target variable

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=3)

# Training the model
model = GaussianNB()
model.fit(X_train, y_train)

# Making predictions
y_pred = model.predict(X_test)

# Evaluating the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")


# יצירת DataFrame חדש שמכיל את התחזיות והערכים האמיתיים
predictions_df = pd.DataFrame({"Actual": y_test, "Predicted": y_pred})

# הוספת אינדקס מחדש לקלות השוואה
predictions_df.reset_index(drop=True, inplace=True)

# הצגת ה-DataFrame
print(predictions_df)

import logging
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
import joblib
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from backend.database import models
from backend.database.dal import DataAccessLayer

# Configure logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def extract_babysitter_data(babysitter):
    return {
        'Babysitter_Id': babysitter.id,
        'Babysitter_Gender': babysitter.user.gender,
        'Babysitter_Skills_Totalnum': len(babysitter.skills),
        #'Babysitter_Relevant_Skills_num': sum(1 for skill in babysitter.skills.id.skill.skill_needs if skill in children_needs),
        
        
        
        # Add other fields as necessary
    }

def extract_skill_data(skill):
    return {
        'id': skill.id,
        # Add other fields as necessary
    }

def extract_need_data(need):
    return {
        'id': need.id,
        'name': need.needname,
        # Add other fields as necessary
    }
    
def extract_favorite_data(favorite):
    return {
        'id': favorite.id,
        'babysitter_id': favorite.babysitter_id,
        'parent_id': favorite.parent_id,
        # Add other fields as necessary
    }

def extract_review_data(review):
    return {
        'id': review.id,
        'babysitter_id': review.babysitter_id,
        'parent_id': review.parent_id,
        # Add other fields as necessary
    }

def extract_contacted_data(contact):
    return {
        'id': contact.id,
        'babysitter_id': contact.babysitter_id,
        'parent_id': contact.parent_id,
        # Add other fields as necessary
    }

def extract_parent_data(parent):
    return {
        'id': parent.id,
        'name': parent.name,
        # Add other fields as necessary
    }

# Start a session
dal = DataAccessLayer()
# Fetch data (might need adjustments)
babysitters = dal.get_all(models.Babysitter)
skills = dal.get_all(models.BabysitterSkill)
needs = dal.get_all(models.ChildrensNeeds)
favorites = dal.get_all(models.Favorite)
reviews = dal.get_all(models.Review)
contacted = dal.get_all(models.Contacted)
parents = dal.get_all(models.Parent)
childrens = dal.get_all(models.ParentsChildrens)


# Extract data from the fetched records
#babysitters_data = [extract_babysitter_data(b) for b in babysitters]
#skills_data = [extract_skill_data(s) for s in skills]

#needs_data = [extract_need_data(n) for n in needs]
#favorites_data = [extract_favorite_data(f) for f in favorites]
#reviews_data = [extract_review_data(r) for r in reviews]
#contacted_data = [extract_contacted_data(c) for c in contacted]
#parents_data = [extract_parent_data(p) for p in parents]

# Convert the extracted data to DataFrames
#df_babysitters = pd.DataFrame(babysitters_data)
#df_skills = pd.DataFrame(skills_data)
#print(df_babysitters, df_skills)
#df_needs = pd.DataFrame(needs_data)
#df_favorites = pd.DataFrame(favorites_data)
#df_reviews = pd.DataFrame(reviews_data)
#df_contacted = pd.DataFrame(contacted_data)
#df_parents = pd.DataFrame(parents_data)


#print (df_babysitters, df_skills, df_needs, df_favorites, df_reviews, df_contacted, parents)
#df_skills['relevant_skills'] = df_skills.apply(lambda row: count_relevant_skills(row, df_needs), axis=1)


data_for_training = []
for parent in parents:
    for babysitter in babysitters:
        babysitter_data = {}
        babysitter_data['Babysitterid'] = babysitter.id
        #babysitter_data['Babysitter_Gender'] = babysitter.user.gender
        babysitter_data['Babysitter_Skills_Totalnum'] = len(babysitter.skills)
        babysitter.skills
        Childs_Needs_Totalnum = 0
        for children in parent.childrens:
           Childs_Needs_Totalnum += len(children.needs_association)
        babysitter_data['Child_Needs_Totalnum'] = Childs_Needs_Totalnum
        babysitter_needs_answers = []
        Babysitter_Relevant_Skills_num = 0
        for skill in babysitter.skills:
            for need in skill.skill.skill_needs:
                    babysitter_needs_answers.append(need.needid)

        for child in parent.childrens:
            for need in child.needs_association:
                if need.needid in babysitter_needs_answers:
                    Babysitter_Relevant_Skills_num += 1
                    
        babysitter_data['Babysitter_Relevant_Skills_num'] = Babysitter_Relevant_Skills_num
        babysitter_data['Favorites_totalnum'] = sum(1 for favorite in favorites if favorite.babysitterid == babysitter.id)
        babysitter_data['Babysitter_Total_Reviews_got'] = sum(1 for review in reviews if review.reviewedid == babysitter.id)
        
        # Contacted label (1 if contacted, 0 otherwise)
        babysitter_data['Contacted'] = 1 if (parent.id, babysitter.id) in [(contact.parentid, contact.babysitterid) for contact in contacted] else 0
        
        data_for_training.append(babysitter_data)

df = pd.DataFrame(data_for_training)
print(df)
# Encoding categorical data
encoder = OneHotEncoder()
#encoded_features = encoder.fit_transform(df[['Babysitter_Gender']]).toarray()
#encoded_feature_labels = encoder.get_feature_names(['Babysitter_Gender'])
#encoded_df = pd.DataFrame(encoded_features, columns=encoded_feature_labels)

# Combine the original DataFrame with the encoded features
#df = pd.concat([df, encoded_df], axis=1).drop(['Babysitter_Gender'], axis=1)
print(df)
# Define features X and labels y
X = df.drop(['Contacted'], axis=1)
y = df['Contacted']

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize and train the Naive Bayes model
nb_model = GaussianNB()
nb_model.fit(X_train, y_train)

# Test the model
y_pred = nb_model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)

print(accuracy)



# Save the model for later use
joblib.dump(nb_model, 'naive_bayes_model.joblib')

# Close the database session



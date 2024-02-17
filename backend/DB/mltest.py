import logging

import crud
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from database import SessionLocal
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import StandardScaler

# Configure logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Start a session
db = SessionLocal()

# Fetch data (simplified examples, replace with actual data fetching and processing)
babysitters = crud.get_babysitters(db)
parents = crud.get_parents(db)
contacted_records = crud.get_all_contacted(db)

# Assuming you have functions or logic to extract skills as binary features
# and have a way to match these features to corresponding parents based on needs

# Placeholder for the feature matrix and target vector
features = []
target = []

# Simplified loop to construct features and target based on your needs
for parent in parents:
    for babysitter in babysitters:
        # Construct feature vector for this babysitter-parent pair
        child_needs = []
        for child in parent.children:
            child_needs.append(child.needs_association)
        skills_for_needs = []
        for child in child_needs:
            for need in child:
                for skill in need.need.need_skills:
                    skills_for_needs.append(skill.skill)
        babysitter_skills = babysitter.skills
        total_number_of_skills = len(babysitter.skills)
        features_vector = [1 if skill in babysitter_skills else 0 for skill in babysitter_skills]
        was_contacted = any(
            contact.parentid == parent.parentid and contact.babysitterid == babysitter.babysitterid
            for contact in contacted_records
        )
        features.append(features_vector)
        target.append(1 if was_contacted else 0)
# Convert lists to DataFrame and Series for use in model

X = pd.DataFrame(features)
y = pd.Series(target)

print(X)
print(y)
print(X.head())
print(y.head())
# Scale the feature matrix
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
# make plt here to visuliaze the current data
# Visualize the number of contacted records


# Splitting the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=16)

# Initializing and training the Gaussian Naive Bayes model
model = GaussianNB()
model.fit(X_train, y_train)

# Making predictions
y_pred = model.predict(X_test)

# Evaluating the model
accuracy = accuracy_score(y_test, y_pred)
logger.info(f"Model Accuracy: {accuracy}")

# Assuming the first plot of the distribution of each skill across all babysitters
fig, ax = plt.subplots(figsize=(10, 6))
sns.countplot(data=X.melt(var_name="Skills", value_name="Presence"), x="Skills", hue="Presence", ax=ax)
plt.xticks(rotation=45, ha="right")
plt.title("Distribution of Skills Presence across Babysitters")
plt.tight_layout()

# Plot the distribution of contacted status
fig, ax = plt.subplots(figsize=(6, 4))
sns.countplot(x=y, ax=ax)
plt.title("Distribution of Contacted Status")
plt.xticks([0, 1], ["Not Contacted", "Contacted"])

plt.show()


plt.figure(figsize=(12, 10))
sns.heatmap(X.corr(), annot=True, fmt=".2f")
plt.title("Feature Correlation Matrix")
plt.show()

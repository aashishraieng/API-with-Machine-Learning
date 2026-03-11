from sklearn.tree import DecisionTreeClassifier
import pickle

# training data
X = [
    [22, 20000],
    [25, 25000],
    [30, 40000],
    [35, 60000],
    [40, 80000],
]

y = [
    "Low",
    "Low",
    "Medium",
    "High",
    "High"
]

model = DecisionTreeClassifier()
model.fit(X, y)

# save model
with open("salary_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved")
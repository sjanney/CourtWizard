import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

# Example dataset (replace with real NBA data)
data = {
    "points": [120, 110, 130, 100, 115],
    "assists": [25, 20, 30, 15, 22],
    "rebounds": [50, 45, 55, 40, 48],
    "winner": [1, 0, 1, 0, 1],  # 1 = Win, 0 = Loss
}

df = pd.DataFrame(data)

# Features and target
X = df[["points", "assists", "rebounds"]]
y = df["winner"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, "models/prediction_model.pkl")
import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib
from pathlib import Path

df = pd.read_csv("data/train.csv")

X = df[["age", "salary"]]
y = df["buy"]

model = LogisticRegression()
model.fit(X, y)

Path("model").mkdir(exist_ok=True)
joblib.dump(model, "model/model.joblib")

print("Model trained and saved to model/model.joblib")

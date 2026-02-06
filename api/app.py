from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()
model = joblib.load("model/model.joblib")

class Input(BaseModel):
    age: int
    salary: int

@app.get("/")
def home():
    return {"message": "MLOps API running"}

@app.post("/predict")
def predict(data: Input):
    prediction = model.predict([[data.age, data.salary]])[0]
    return {"prediction": int(prediction)}

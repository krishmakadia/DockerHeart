from fastapi import FastAPI
import joblib
import numpy as np
from pydantic import BaseModel

# Load the trained model
model = joblib.load("model.joblib")

# Initialize FastAPI app
app = FastAPI()

# Define the input data format
class HeartDiseaseInput(BaseModel):
    age: int
    sex: int
    cp: int
    trestbps: int
    chol: int
    fbs: int
    restecg: int
    thalach: int
    exang: int
    oldpeak: float
    slope: int
    ca: int
    thal: int

# Define API endpoint
@app.post("/predict")
def predict_heart_disease(data: HeartDiseaseInput):
    # Convert input data to a NumPy array
    input_data = np.array([[data.age, data.sex, data.cp, data.trestbps, data.chol, data.fbs,
                            data.restecg, data.thalach, data.exang, data.oldpeak, data.slope,
                            data.ca, data.thal]])

    # Make prediction
    prediction = model.predict(input_data)
    result = "Heart Disease Detected" if prediction[0] == 1 else "No Heart Disease"

    return {"prediction": result}


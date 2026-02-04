from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Call Analyzer AI")

class AudioRequest(BaseModel):
    audio_base64: str
    language: str

@app.get("/")
def home():
    return {"status": "API running"}

@app.post("/predict")
def predict(request: AudioRequest):
    return {
        "classification": "AI",
        "confidence": 0.50,
        "explanation": "Model not loaded yet"
    }

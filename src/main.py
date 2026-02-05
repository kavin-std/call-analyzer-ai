from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class AudioRequest(BaseModel):
    audio_base64: str

@app.get("/")
def root():
    return {"status": "API running"}

@app.post("/detect-voice")
def detect_voice(data: AudioRequest):
    return {
        "language": "unknown",
        "classification": "processing",
        "risk_score": 0.0
    }

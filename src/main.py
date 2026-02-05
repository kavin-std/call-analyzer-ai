from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel

app = FastAPI()

API_KEY = "gomakakey86"

class AudioRequest(BaseModel):
    audio_base64: str

@app.get("/")
def root():
    return {"status": "API running"}

@app.post("/detect-voice")
def detect_voice(
    data: AudioRequest,
    x_api_key: str = Header(None)
):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    return {
        "language": "unknown",
        "classification": "processing",
        "risk_score": 0.0
    }

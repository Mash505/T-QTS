from fastapi import FastAPI

app = FastAPI(title="T-QTS Core Engine")

@app.get("/")
def home():
    return {
        "system": "T-QTS",
        "status": "running",
        "phase": "1 - foundation"
    }

@app.get("/health")
def health():
    return {"status": "ok"}

from fastapi import FastAPI
from orchestrator.core import Orchestrator

app = FastAPI(title="T-QTS Phase 2")

orchestrator = Orchestrator()

@app.get("/")
def home():
    return {"system": "T-QTS", "phase": 2}

@app.get("/run")
def run():
    return orchestrator.run_cycle()

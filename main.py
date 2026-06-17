from fastapi import FastAPI
from orchestrator.core import Orchestrator

app = FastAPI(title="T-QTS Phase 3")

orchestrator = Orchestrator()

@app.get("/")
def home():
    return {"system": "T-QTS", "phase": 3}

@app.get("/run")
def run():
    return orchestrator.run_cycle()

@app.get("/memory")
def memory():
    return orchestrator.memory.get_all()

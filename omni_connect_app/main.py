from fastapi import FastAPI
from omnidim_sdk import list_all_agents

app = FastAPI()

@app.get("/agents")
def get_agents():
    return list_all_agents()

from fastapi import FastAPI
from dotenv import load_dotenv
import os
from omnidimension import Client

# Load .env file
load_dotenv()

# Get API Key from environment
api_key = os.getenv("OMNIDIM_API_KEY")
print("Loaded API key:", api_key)
# Initialize OmniDimension client
client = Client(api_key)

# FastAPI app instance
app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to OmniConnect - Voice Assistant"}

@app.get("/agents")
def get_all_agents():
    try:
        agents = client.agent.list()
        return {"agents": agents}
    except Exception as e:
        return {"error": str(e)}

@app.get("/agent/{agent_id}")
def get_agent_by_id(agent_id: str):
    try:
        agent = client.agent.get(agent_id)
        return {"agent": agent}
    except Exception as e:
        return {"error": str(e)}

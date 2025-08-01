# omnidim_sdk.py
import os
from dotenv import load_dotenv
from omnidimension import Client

load_dotenv()  # Loads variables from .env file

# Initialize OmniDimension Client
api_key = os.getenv('OP35dWxsOtNcu6uxK3sUhFz4sn7Q4RLPtA5pHpMNdbQA')
client = Client(api_key)

def list_all_agents():
    return client.agent.list()

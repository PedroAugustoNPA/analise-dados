import os
import requests
from dotenv import load_dotenv
import json

load_dotenv()

class RiotApi:
    def __init__(self):
        self.session = requests.Session()
        self.apiKey = os.getenv("RIOT_API_KEY")
        self.session.headers.update({"X-Riot-Token": self.apiKey})
    

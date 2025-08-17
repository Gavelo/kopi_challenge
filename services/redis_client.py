import redis
import os
import json
from dotenv import load_dotenv
from typing import List, Dict

load_dotenv()


redis_client = redis.Redis(host=os.getenv("REDIS_HOST"), port=6379, db=0, decode_responses=True)

def get_conversation_history(conversation_id: str) -> List[Dict]:
    history_json = redis_client.get(conversation_id)
    if history_json:
        return json.loads(history_json)
    return []

def save_conversation_history(conversation_id: str, history: List[Dict]):
    """Guarda el historial de una conversación en Redis con una expiración de 24 horas."""
    history_json = json.dumps(history)
    redis_client.set(conversation_id, history_json, ex=86400)
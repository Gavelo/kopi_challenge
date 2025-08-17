from pydantic import BaseModel
from typing import List, Literal, Optional

class ChatMessage(BaseModel):
    role: Literal["user", "bot"]
    message: str

class APIRequest(BaseModel):
    conversation_id: Optional[str] = None
    message: str

class APIResponse(BaseModel):
    conversation_id: str
    message: List[ChatMessage]
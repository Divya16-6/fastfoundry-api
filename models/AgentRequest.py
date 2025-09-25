from pydantic import BaseModel
from typing import List, Dict, Optional

class CreateAgentRequest(BaseModel):
    name: str
    model: str = "gpt-4o-mini"
    instructions: str
    tools: Optional[List[Dict]] = None

class UpdateAgentRequest(BaseModel):
    name: str
    model: str
    instructions: str
from pydantic import BaseModel

class CreateAgentRequest(BaseModel):
    name: str
    model: str = "gpt-4o-mini"
    instructions: str

class UpdateAgentRequest(BaseModel):
    name: str
    model: str
    instructions: str
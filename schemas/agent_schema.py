from pydantic import BaseModel
from typing import List


class AgentSpec(BaseModel):
    name: str
    purpose: str
    tools: List[str]
    workflow: List[str]
    model: str
from typing import Literal
from pydantic import BaseModel


class StepSpec(BaseModel):
    name: str
    instruction: str


class AgentLimits(BaseModel):
    max_steps: int = 6
    timeout_seconds: int = 120


class AgentSpec(BaseModel):
    name: str
    purpose: str
    model: str = "qwen3:4b"
    tools: list[str]
    workflow: list[StepSpec]
    output_style: Literal[
        "text",
        "report",
        "json",
    ] = "text"
    limits: AgentLimits = AgentLimits()
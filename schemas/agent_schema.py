from typing import Literal
from pydantic import BaseModel, Field, field_validator


class StepSpec(BaseModel):
    name: str = Field(min_length=1, max_length=60)
    instruction: str = Field(min_length=1, max_length=500)


class AgentLimits(BaseModel):
    max_steps: int = Field(default=5, ge=1, le=10)
    timeout_seconds: int = Field(default=300, ge=10, le=600)


class AgentSpec(BaseModel):
    name: str = Field(min_length=1, max_length=80)
    purpose: str = Field(min_length=1, max_length=500)
    model: str = "qwen3:4b"
    tools: list[str] = Field(default_factory=list, max_length=5)
    workflow: list[StepSpec] = Field(min_length=1, max_length=10)
    output_style: Literal["text", "report", "json"] = "text"
    limits: AgentLimits = Field(default_factory=AgentLimits)

    @field_validator("tools")
    @classmethod
    def remove_duplicate_tools(cls, value: list[str]) -> list[str]:
        return list(dict.fromkeys(value))


class AgentResult(BaseModel):
    agent_name: str
    purpose: str
    status: Literal["success", "failed"]
    output: str
    duration_ms: int

from pydantic import BaseModel, Field
from schemas.agent_schema import AgentSpec


class AgentTeam(BaseModel):
    team_name: str = Field(min_length=1, max_length=80)
    objective: str = Field(min_length=1, max_length=500)
    agents: list[AgentSpec] = Field(min_length=1, max_length=6)


class TeamRunResult(BaseModel):
    team_name: str
    objective: str
    final_output: str
    agent_results: list
    duration_ms: int

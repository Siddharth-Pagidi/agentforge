from ollama import Client
from config import MAX_TEAM_SIZE, OLLAMA_HOST, OLLAMA_MODEL
from schemas.team_schema import AgentTeam
from tools.registry import ToolRegistry


class MasterOrchestrator:
    def __init__(self, tool_registry: ToolRegistry) -> None:
        self.client = Client(host=OLLAMA_HOST)
        self.tools = tool_registry

    def create_team(self, request: str) -> AgentTeam:
        if not request.strip():
            raise ValueError("The request cannot be empty.")

        system_prompt = f"""You are the master architect for AgentForge.
Design a small team of specialized AI agents for the user's request.
Create no more than {MAX_TEAM_SIZE} agents.
Each agent must have a distinct purpose and a practical workflow.
Use the fewest agents necessary.
Do not generate executable code.
Available external tools:
{self.tools.descriptions()}
Only include tools listed above. If no tools are available, every tools list must be empty.
Each agent must use model {OLLAMA_MODEL}.
Return only data matching the supplied JSON schema."""

        response = self.client.chat(
            model=OLLAMA_MODEL,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": request},
            ],
            format=AgentTeam.model_json_schema(),
            options={"temperature": 0},
        )

        content = response.message.content
        if not content:
            raise RuntimeError("Ollama returned an empty team specification.")

        team = AgentTeam.model_validate_json(content)
        team.agents = team.agents[:MAX_TEAM_SIZE]

        for agent in team.agents:
            agent.model = OLLAMA_MODEL
            self.tools.validate(agent.tools)

        return team

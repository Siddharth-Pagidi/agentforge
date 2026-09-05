import asyncio
from ollama import AsyncClient
from config import OLLAMA_HOST, OLLAMA_MODEL
from schemas.agent_schema import AgentResult
from schemas.team_schema import AgentTeam


class Synthesizer:
    def __init__(self) -> None:
        self.client = AsyncClient(host=OLLAMA_HOST)

    async def synthesize(
        self,
        team: AgentTeam,
        task: str,
        results: list[AgentResult],
    ) -> str:
        combined = "\n\n".join(
            f"AGENT: {result.agent_name}\n"
            f"PURPOSE: {result.purpose}\n"
            f"STATUS: {result.status}\n"
            f"OUTPUT:\n{result.output}"
            for result in results
        )

        system_prompt = """You are the final synthesizer for a multi-agent system.
Combine the useful findings into one clear, coherent final answer.
Remove repetition and resolve obvious inconsistencies.
Do not invent facts, citations, tool usage, or research that the agents did not provide.
Mention important limitations when an agent failed."""

        response = await asyncio.wait_for(
            self.client.chat(
                model=OLLAMA_MODEL,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {
                        "role": "user",
                        "content": (
                            f"Team: {team.team_name}\n"
                            f"Objective: {team.objective}\n"
                            f"Original task: {task}\n\n"
                            f"Agent results:\n{combined}"
                        ),
                    },
                ],
                options={"temperature": 0.1},
            ),
            timeout=180,
        )
        return response.message.content or "No final output returned."

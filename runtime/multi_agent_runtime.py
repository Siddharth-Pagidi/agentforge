import asyncio
import time
from runtime.agent_runtime import AgentRuntime
from schemas.agent_schema import AgentResult
from schemas.team_schema import AgentTeam


class MultiAgentRuntime:
    async def run_team(self, team: AgentTeam, task: str) -> tuple[list[AgentResult], int]:
        started = time.perf_counter()
        jobs = [
            AgentRuntime(agent).run(task)
            for agent in team.agents
        ]
        results = await asyncio.gather(*jobs)
        duration_ms = int((time.perf_counter() - started) * 1000)
        return results, duration_ms

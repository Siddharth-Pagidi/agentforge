import time
from orchestrator.master_orchestrator import MasterOrchestrator
from runtime.multi_agent_runtime import MultiAgentRuntime
from runtime.registry import Registry
from runtime.synthesizer import Synthesizer
from schemas.team_schema import AgentTeam
from tools.registry import ToolRegistry


class AgentForge:
    def __init__(self) -> None:
        tools = ToolRegistry()
        self.orchestrator = MasterOrchestrator(tools)
        self.multi_runtime = MultiAgentRuntime()
        self.synthesizer = Synthesizer()
        self.registry = Registry()

    async def run(self, request: str, task: str | None = None) -> dict:
        overall_started = time.perf_counter()
        actual_task = task or request

        team: AgentTeam = self.orchestrator.create_team(request)
        self.registry.save_team(team)

        agent_results, parallel_duration_ms = await self.multi_runtime.run_team(
            team,
            actual_task,
        )
        final_output = await self.synthesizer.synthesize(
            team,
            actual_task,
            agent_results,
        )

        total_duration_ms = int((time.perf_counter() - overall_started) * 1000)
        run_id = self.registry.save_run(
            team,
            actual_task,
            final_output,
            total_duration_ms,
        )

        return {
            "run_id": run_id,
            "team": team,
            "agent_results": agent_results,
            "parallel_duration_ms": parallel_duration_ms,
            "total_duration_ms": total_duration_ms,
            "final_output": final_output,
        }

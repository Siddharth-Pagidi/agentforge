import asyncio
import time
from ollama import AsyncClient
from config import OLLAMA_HOST
from schemas.agent_schema import AgentResult, AgentSpec


class AgentRuntime:
    def __init__(self, spec: AgentSpec) -> None:
        self.spec = spec
        self.client = AsyncClient(host=OLLAMA_HOST)

    async def run(self, task: str) -> AgentResult:
        started = time.perf_counter()
        workflow = "\n".join(
            f"{number}. {step.name}: {step.instruction}"
            for number, step in enumerate(self.spec.workflow, start=1)
        )

        system_prompt = f"""You are {self.spec.name}.
Your purpose is: {self.spec.purpose}
Follow this workflow:
{workflow}
Focus only on your specialty.
Produce useful content for another AI that will combine your work with other agents.
Do not claim to have used tools, searched the web, or accessed current data unless a tool result was actually supplied.
Output style: {self.spec.output_style}."""

        try:
            response = await asyncio.wait_for(
                self.client.chat(
                    model=self.spec.model,
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": task},
                    ],
                    options={"temperature": 0.2},
                ),
                timeout=self.spec.limits.timeout_seconds,
            )
            output = response.message.content or "No output returned."
            status = "success"
        except Exception as exc:
            output = f"{type(exc).__name__}: {exc}"
            status = "failed"

        duration_ms = int((time.perf_counter() - started) * 1000)
        return AgentResult(
            agent_name=self.spec.name,
            purpose=self.spec.purpose,
            status=status,
            output=output,
            duration_ms=duration_ms,
        )

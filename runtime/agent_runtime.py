import asyncio

from ollama import AsyncClient

from config import OLLAMA_HOST


class AgentRuntime:

    def __init__(self, spec):
        self.spec = spec

        self.client = AsyncClient(
            host=OLLAMA_HOST
        )

    async def run(
        self,
        task: str,
    ) -> str:

        workflow = "\n".join(
            (
                f"{number}. {step.name}: "
                f"{step.instruction}"
            )
            for number, step in enumerate(
                self.spec.workflow,
                start=1,
            )
        )

        system_prompt = f"""
You are {self.spec.name}.

Purpose:
{self.spec.purpose}

Follow this workflow:
{workflow}

Output style:
{self.spec.output_style}

Complete the user's task concisely and accurately.

Do not claim to have searched the web because this
local version does not have an implemented web-search
tool yet.

If the task requires current information, clearly say
that live web search is unavailable.
"""

        response = await asyncio.wait_for(
            self.client.chat(
                model=self.spec.model,
                messages=[
                    {
                        "role": "system",
                        "content": system_prompt,
                    },
                    {
                        "role": "user",
                        "content": task,
                    },
                ],
                options={
                    "temperature": 0.2,
                },
            ),
            timeout=self.spec.limits.timeout_seconds,
        )

        content = response.message.content

        if not content:
            raise RuntimeError(
                "The generated agent returned no output."
            )

        return content
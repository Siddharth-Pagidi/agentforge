from ollama import Client

from config import OLLAMA_HOST, OLLAMA_MODEL
from schemas.agent_schema import AgentSpec


class AgentFactory:

    def __init__(self):
        self.client = Client(
            host=OLLAMA_HOST
        )

    def create_agent(
        self,
        request: str,
    ) -> AgentSpec:

        if not request.strip():
            raise ValueError(
                "The agent request cannot be empty."
            )

        system_prompt = """
You are the architect for AgentForge.

Design a small and efficient AI agent for the user's
request.

Return an agent specification matching the supplied
JSON schema.

Requirements:
- Use a short, descriptive agent name.
- Give the agent one clear purpose.
- Use the fewest workflow steps necessary.
- Do not generate Python code.
- Do not claim that unavailable tools exist.
- The only currently available tool is web_search.
- Only include web_search when current external
  information is required.
- Use conservative limits.
"""

        response = self.client.chat(
            model=OLLAMA_MODEL,
            messages=[
                {
                    "role": "system",
                    "content": system_prompt,
                },
                {
                    "role": "user",
                    "content": request,
                },
            ],
            format=AgentSpec.model_json_schema(),
            options={
                "temperature": 0,
            },
        )

        content = response.message.content

        if not content:
            raise RuntimeError(
                "Ollama returned an empty agent specification."
            )

        spec = AgentSpec.model_validate_json(
            content
        )

        spec.model = OLLAMA_MODEL

        return spec
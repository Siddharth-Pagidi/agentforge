import asyncio

from orchestrator.agent_factory import AgentFactory

from runtime.agent_runtime import AgentRuntime

from runtime.registry import AgentRegistry


async def main():

    request = input(
        "Create what kind of agent?\n> "
    )

    factory = AgentFactory()

    registry = AgentRegistry()

    spec = factory.create_agent(
        request
    )

    registry.register(
        spec
    )

    runtime = AgentRuntime(
        spec
    )

    result = await runtime.run(
        request
    )

    print("\nAgent Generated:")
    print(spec)

    print("\nResult:")
    print(result)


if __name__ == "__main__":
    asyncio.run(main())
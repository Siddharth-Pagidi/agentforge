import asyncio

from orchestrator.planner import Planner
from orchestrator.agent_factory import AgentFactory

from runtime.registry import AgentRegistry
from runtime.agent_runtime import AgentRuntime

from tools.memory import Memory


async def main():

    user_request = input(
        "What agent would you like me to create?\n> "
    )

    planner = Planner()

    factory = AgentFactory()

    registry = AgentRegistry()

    memory = Memory()

    agent_type = planner.analyze_task(
        user_request
    )

    agent_spec = factory.create_agent(
        agent_type
    )

    registry.register(
        agent_spec
    )

    runtime = AgentRuntime(
        agent_spec
    )

    result = await runtime.run(
        user_request
    )

    memory.save(
        result
    )

    print("\nRegistered Agents:")
    print(
        registry.list_agents()
    )

    print("\nHistory:")
    print(
        memory.get_history()
    )


if __name__ == "__main__":
    asyncio.run(main())

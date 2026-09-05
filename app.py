import asyncio
from service import AgentForge


async def main() -> None:
    forge = AgentForge()

    request = input("Describe the AI team you want:\n> ").strip()
    task = input(
        "Give the team a task, or press Enter to reuse the description:\n> "
    ).strip()

    print("\nCreating the team and running agents in parallel...\n")
    result = await forge.run(request, task or None)
    team = result["team"]

    print("TEAM GENERATED")
    print(f"Name: {team.team_name}")
    print(f"Objective: {team.objective}")
    print("Agents:")
    for agent in team.agents:
        print(f"  - {agent.name}: {agent.purpose}")

    print("\nINDIVIDUAL RESULTS")
    for agent_result in result["agent_results"]:
        print(f"\n[{agent_result.agent_name}] {agent_result.status}")
        print(agent_result.output)

    print("\nFINAL SYNTHESIZED OUTPUT")
    print(result["final_output"])

    print(
        f"\nParallel agent time: {result['parallel_duration_ms']} ms"
        f"\nTotal time: {result['total_duration_ms']} ms"
        f"\nRun ID: {result['run_id']}"
    )


if __name__ == "__main__":
    asyncio.run(main())

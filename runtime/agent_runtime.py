class AgentRuntime:

    def __init__(self, spec):
        self.spec = spec

    async def run(self, task):

        print("\n========================")
        print(f"Agent: {self.spec.name}")
        print("========================")

        print(f"Task: {task}\n")

        for step in self.spec.workflow:
            print(f"Running step: {step}")

        print("\nTask Complete")

        return {
            "agent": self.spec.name,
            "task": task,
            "status": "success"
        }
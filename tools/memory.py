class Memory:

    def __init__(self):

        self.runs = []

    def save_run(
        self,
        agent_name,
        task,
        result
    ):

        self.runs.append(
            {
                "agent": agent_name,
                "task": task,
                "result": result
            }
        )

    def get_all_runs(self):

        return self.runs
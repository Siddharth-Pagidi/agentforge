class TeamMemory:

    def __init__(self):
        self.history = []

    def save(self, task, result):
        self.history.append(
            {
                "task": task,
                "result": result
            }
        )

    def get_history(self):
        return self.history
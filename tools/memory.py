class Memory:

    def __init__(self):
        self.history = []

    def save(self, item):
        self.history.append(item)

    def get_history(self):
        return self.history

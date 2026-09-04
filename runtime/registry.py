class AgentRegistry:

    def __init__(self):
        self.agents = {}

    def register(self, agent_spec):
        self.agents[agent_spec.name] = agent_spec

    def get(self, name):
        return self.agents.get(name)

    def list_agents(self):
        return list(self.agents.keys())

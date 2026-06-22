from typing import List

class Agent:
    def __init__(self, name):
        self.name = name

    def process(self, task):
        return f"{self.name} processed: {task}"


class NeuralMesh:
    def __init__(self):
        self.agents = []

    def register_agent(self, agent):
        self.agents.append(agent)

    def route_task(self, task):
        responses = []

        for agent in self.agents:
            responses.append(agent.process(task))

        return responses


if __name__ == "__main__":
    mesh = NeuralMesh()

    mesh.register_agent(Agent("Planner"))
    mesh.register_agent(Agent("Retriever"))
    mesh.register_agent(Agent("Reasoner"))
    mesh.register_agent(Agent("Validator"))

    task = "Generate a scalable GenAI system design"

    results = mesh.route_task(task)

    for result in results:
        print(result)

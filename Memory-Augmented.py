from collections import deque
from datetime import datetime


class EpisodicMemory:
    def __init__(self, capacity=10):
        self.memory = deque(maxlen=capacity)

    def store(self, query, response):
        self.memory.append({
            "timestamp": datetime.now(),
            "query": query,
            "response": response
        })

    def retrieve(self, query):
        for item in reversed(self.memory):
            if query.lower() in item["query"].lower():
                return item["response"]
        return None


class MemoryAgent:
    def __init__(self):
        self.memory = EpisodicMemory()

    def process(self, query):
        previous = self.memory.retrieve(query)

        if previous:
            return f"Retrieved from memory: {previous}"

        response = f"Generated response for: {query}"
        self.memory.store(query, response)

        return response


if __name__ == "__main__":
    agent = MemoryAgent()

    print(agent.process("Explain RAG architecture"))
    print(agent.process("Explain multi-agent systems"))
    print(agent.process("Explain RAG architecture"))

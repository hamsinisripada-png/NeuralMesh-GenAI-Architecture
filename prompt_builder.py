def build_prompt(context, question):
    return f"""
You are an AI assistant.

Context:
{context}

Question:
{question}

Answer:
"""

"""
This script demonstrates a basic LLM-style workflow.
(No real API call – focuses on understanding the flow)
"""

def build_prompt(user_question, context):
    prompt = f"""
    Context:
    {context}

    Question:
    {user_question}

    Answer:
    """
    return prompt


if __name__ == "__main__":
    context = "LLMs are used in backend systems to generate intelligent responses."
    question = "What is an LLM?"

    prompt = build_prompt(question, context)
    print("Generated Prompt:")
    print(prompt)

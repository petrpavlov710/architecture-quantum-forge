from app.rag.mistral_client import call_mistral
from app.rag.prompt_templates import COT_SYSTEM_PROMPT, FEW_SHOT_EXAMPLES


def call_llm(query, context) -> str:
    context = "\n".join([f"{doc.page_content}" for doc in context])

    final_prompt = f"""
        {COT_SYSTEM_PROMPT}
        {FEW_SHOT_EXAMPLES}

        Контекст:
        {context}

        Q: {query}
        A:
    """

    return call_mistral(final_prompt)

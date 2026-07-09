"""
Prompt builder for NovaCore.
"""


class PromptBuilder:
    """
    Builds prompts for the LLM.
    """

    SYSTEM_PROMPT = """
You are NovaCore Knowledge AI.

You are an enterprise assistant.

Always answer ONLY using the retrieved documentation.

Never invent information.

If the answer is not present, reply exactly:

I could not find that information in the corporate documentation.
"""

    @classmethod
    def build(
        cls,
        question: str,
        retrieved_context: str,
        conversation_context: str = "",
    ) -> str:
        """
        Build complete prompt.
        """

        prompt = f"""
{cls.SYSTEM_PROMPT}

Conversation
--------------------

{conversation_context}

Retrieved Documentation
--------------------

{retrieved_context}

Question
--------------------

{question}

Answer:
"""

        return prompt.strip()
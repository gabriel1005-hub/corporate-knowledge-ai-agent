"""
Conversation service.

Manages chat history independently from Streamlit.
"""

from uuid import uuid4


class ConversationService:
    """
    Handles conversation state.
    """

    def __init__(self):

        self._conversation = []

        self._id = str(uuid4())

    @property
    def id(self):

        return self._id

    @property
    def history(self):

        return self._conversation

    def add_user_message(
        self,
        message: str,
    ):

        self._conversation.append(
            {
                "role": "user",
                "content": message,
            }
        )

    def add_assistant_message(
        self,
        message: str,
    ):

        self._conversation.append(
            {
                "role": "assistant",
                "content": message,
            }
        )

    def clear(self):

        self._conversation = []

        self._id = str(uuid4())

    def build_context(
        self,
        max_messages: int = 6,
    ) -> str:
        """
        Returns the latest conversation
        formatted for the LLM.
        """

        messages = self._conversation[
            -max_messages:
        ]

        context = []

        for message in messages:

            role = message[
                "role"
            ].capitalize()

            context.append(
                f"{role}: {message['content']}"
            )

        return "\n".join(
            context
        )
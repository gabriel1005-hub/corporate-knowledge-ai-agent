"""
Conversation service.

Manages conversations independently from the UI.
"""

from dataclasses import dataclass, field
from datetime import datetime
from uuid import uuid4


@dataclass(slots=True)
class Message:
    """
    Chat message.
    """

    role: str
    content: str
    timestamp: datetime = field(
        default_factory=datetime.now
    )


class ConversationService:
    """
    Conversation manager.
    """

    def __init__(self):

        self.new_conversation()

    # -------------------------------------------------

    def new_conversation(self):

        self.id = str(
            uuid4()
        )

        self.messages = []

    # -------------------------------------------------

    def add_user(
        self,
        content: str,
    ):

        self.messages.append(

            Message(
                role="user",
                content=content,
            )

        )

    # -------------------------------------------------

    def add_assistant(
        self,
        content: str,
    ):

        self.messages.append(

            Message(
                role="assistant",
                content=content,
            )

        )

    # -------------------------------------------------

    def history(
        self,
        limit: int = 8,
    ):

        return self.messages[-limit:]

    # -------------------------------------------------

    def build_context(
        self,
        limit: int = 8,
    ) -> str:
        """
        Build conversational context.
        """

        history = self.history(
            limit
        )

        lines = []

        for message in history:

            role = (
                "User"
                if message.role == "user"
                else "Assistant"
            )

            lines.append(
                f"{role}: {message.content}"
            )

        return "\n".join(
            lines
        )

    # -------------------------------------------------

    def clear(self):

        self.new_conversation()
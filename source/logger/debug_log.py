from typing import Any

from source.base.base import AbstractHandler


class DebugLog(AbstractHandler):
    """Debug Logger"""

    def handle(self, handler: str, message: str) -> Any:
        if handler.lower() == self.DEBUG.lower():
            print(message)
        else:
            super().handle(handler, message)

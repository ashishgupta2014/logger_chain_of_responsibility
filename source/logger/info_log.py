from typing import Any

from source.base.base import AbstractHandler


class InfoLog(AbstractHandler):
    """Info Logger"""

    def handle(self, handler: str, message: str) -> Any:
        if handler.lower() == self.INFO.lower():
            print(message)
        else:
            super().handle(handler, message)

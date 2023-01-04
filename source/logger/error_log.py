from typing import Any

from source.base.base import AbstractHandler


class ErrorLog(AbstractHandler):
    """Error Logger"""

    def handle(self, handler: str, message: str) -> Any:
        if handler.lower() == self.ERROR.lower():
            print(message)
        else:
            super().handle(handler, message)

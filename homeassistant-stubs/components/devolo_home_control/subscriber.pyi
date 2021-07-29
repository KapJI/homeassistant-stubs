from typing import Any, Callable

_LOGGER: Any

class Subscriber:
    name: Any
    callback: Any
    def __init__(self, name: str, callback: Callable) -> None: ...
    def update(self, message: str) -> None: ...

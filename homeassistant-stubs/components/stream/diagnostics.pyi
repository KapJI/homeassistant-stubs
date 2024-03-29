from _typeshed import Incomplete
from typing import Any

class Diagnostics:
    _counter: Incomplete
    _values: Incomplete
    def __init__(self) -> None: ...
    def increment(self, key: str) -> None: ...
    def set_value(self, key: str, value: Any) -> None: ...
    def as_dict(self) -> dict[str, Any]: ...

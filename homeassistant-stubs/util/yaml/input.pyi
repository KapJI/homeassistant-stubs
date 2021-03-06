from .objects import Input as Input
from typing import Any

class UndefinedSubstitution(Exception):
    input: Any
    def __init__(self, input_name: str) -> None: ...

def extract_inputs(obj: Any) -> set[str]: ...
def _extract_inputs(obj: Any, found: set[str]) -> None: ...
def substitute(obj: Any, substitutions: dict[str, Any]) -> Any: ...

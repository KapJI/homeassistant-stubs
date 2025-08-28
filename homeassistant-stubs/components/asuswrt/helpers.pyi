from _typeshed import Incomplete
from typing import Any, TypeVar

T = TypeVar('T', dict[str, Any], list[Any], None)
TRANSLATION_MAP: Incomplete

def clean_dict(raw: dict[str, Any]) -> dict[str, Any]: ...
def translate_to_legacy(raw: T) -> T: ...

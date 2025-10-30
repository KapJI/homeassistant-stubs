from _typeshed import Incomplete
from typing import Any

TRANSLATION_MAP: Incomplete

def clean_dict(raw: dict[str, Any]) -> dict[str, Any]: ...
def translate_to_legacy[T: (dict[str, Any], list[Any], None)](raw: T) -> T: ...

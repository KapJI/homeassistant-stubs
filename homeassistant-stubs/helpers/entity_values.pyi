from homeassistant.core import split_entity_id as split_entity_id
from typing import Any

class EntityValues:
    _cache: Any
    _exact: Any
    _domain: Any
    _glob: Any
    def __init__(self, exact: Union[dict[str, dict[str, str]], None] = ..., domain: Union[dict[str, dict[str, str]], None] = ..., glob: Union[dict[str, dict[str, str]], None] = ...) -> None: ...
    def get(self, entity_id: str) -> dict[str, str]: ...

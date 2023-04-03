from _typeshed import Incomplete
from homeassistant.core import split_entity_id as split_entity_id

class EntityValues:
    _cache: Incomplete
    _exact: Incomplete
    _domain: Incomplete
    _glob: Incomplete
    def __init__(self, exact: dict[str, dict[str, str]] | None = ..., domain: dict[str, dict[str, str]] | None = ..., glob: dict[str, dict[str, str]] | None = ...) -> None: ...
    def get(self, entity_id: str) -> dict[str, str]: ...

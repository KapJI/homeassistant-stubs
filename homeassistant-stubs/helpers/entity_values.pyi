from _typeshed import Incomplete
from homeassistant.core import split_entity_id as split_entity_id

class EntityValues:
    _cache: Incomplete
    _exact: Incomplete
    _domain: Incomplete
    _glob: Incomplete
    def __init__(self, exact: Union[dict[str, dict[str, str]], None] = ..., domain: Union[dict[str, dict[str, str]], None] = ..., glob: Union[dict[str, dict[str, str]], None] = ...) -> None: ...
    def get(self, entity_id: str) -> dict[str, str]: ...

from .registry import BaseRegistryItems as BaseRegistryItems
from _typeshed import Incomplete
from dataclasses import dataclass
from typing import TypeVar

@dataclass(slots=True, frozen=True, kw_only=True)
class NormalizedNameBaseRegistryEntry:
    name: str
    normalized_name: str
    def __init__(self, *, name, normalized_name) -> None: ...
_VT = TypeVar('_VT', bound=NormalizedNameBaseRegistryEntry)

def normalize_name(name: str) -> str: ...

class NormalizedNameBaseRegistryItems(BaseRegistryItems[_VT]):
    _normalized_names: Incomplete
    def __init__(self) -> None: ...
    def _unindex_entry(self, key: str, replacement_entry: _VT | None = None) -> None: ...
    def _index_entry(self, key: str, entry: _VT) -> None: ...
    def get_by_name(self, name: str) -> _VT | None: ...

from collections.abc import Mapping
from typing import Any, Generic, TypeVar

__all__ = ['EventType']

_DataT = TypeVar('_DataT', bound=Mapping[str, Any], default=Mapping[str, Any])

class EventType(Generic[_DataT]):
    def __init__(self, value: str, /) -> None: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __eq__(self, value: object) -> bool: ...
    def __getitem__(self, index: int) -> str: ...

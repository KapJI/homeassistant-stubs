from enum import Enum
from typing import Any, TypeVar

_StrEnumSelfT = TypeVar('_StrEnumSelfT', bound='StrEnum')

class StrEnum(str, Enum):
    def __new__(cls, value: str, *args: Any, **kwargs: Any) -> _StrEnumSelfT: ...
    def __str__(self) -> str: ...
    @staticmethod
    def _generate_next_value_(name: str, start: int, count: int, last_values: list[Any]) -> Any: ...

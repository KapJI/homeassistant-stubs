from collections.abc import Callable
from enum import Enum
from typing import Any, TypeVar

_LruCacheT = TypeVar('_LruCacheT', bound=Callable)

def lru_cache(func: _LruCacheT) -> _LruCacheT: ...
_EnumT = TypeVar('_EnumT', bound=Enum)

def try_parse_enum(cls, value: Any) -> _EnumT | None: ...

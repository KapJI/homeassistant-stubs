from collections.abc import Callable as Callable, Iterable, Mapping
from homeassistant.core import callback as callback
from typing import Any, TypeVar, overload

REDACTED: str
_T = TypeVar('_T')
_ValueT = TypeVar('_ValueT')

def partial_redact(x: str | Any, unmasked_prefix: int = 4, unmasked_suffix: int = 4) -> str: ...
@overload
def async_redact_data(data: Mapping, to_redact: Iterable[Any] | Mapping[Any, Callable[[_ValueT], _ValueT]]) -> dict: ...
@overload
def async_redact_data(data: _T, to_redact: Iterable[Any] | Mapping[Any, Callable[[_ValueT], _ValueT]]) -> _T: ...

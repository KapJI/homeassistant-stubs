from . import EvilGeniusEntity as EvilGeniusEntity
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable, Coroutine
from typing import Any, Concatenate, TypeVar

_EvilGeniusEntityT = TypeVar('_EvilGeniusEntityT', bound=EvilGeniusEntity)
_R = TypeVar('_R')
_P: Incomplete

def update_when_done(func: Callable[Concatenate[_EvilGeniusEntityT, _P], Awaitable[_R]]) -> Callable[Concatenate[_EvilGeniusEntityT, _P], Coroutine[Any, Any, _R]]: ...

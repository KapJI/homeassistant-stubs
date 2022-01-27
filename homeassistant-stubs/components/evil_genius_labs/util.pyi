from . import EvilGeniusEntity as EvilGeniusEntity
from collections.abc import Awaitable as Awaitable, Callable as Callable, Coroutine
from typing import Any, TypeVar
from typing_extensions import Concatenate as Concatenate

_T = TypeVar('_T', bound=EvilGeniusEntity)
_R = TypeVar('_R')
_P: Any

def update_when_done(func: Callable[Concatenate[_T, _P], Awaitable[_R]]) -> Callable[Concatenate[_T, _P], Coroutine[Any, Any, _R]]: ...

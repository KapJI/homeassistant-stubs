from . import EvilGeniusEntity as EvilGeniusEntity
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable, Coroutine
from typing import Any, TypeVar
from typing_extensions import Concatenate as Concatenate

_T = TypeVar('_T', bound=EvilGeniusEntity)
_R = TypeVar('_R')
_P: Incomplete

def update_when_done(func: Callable[Concatenate[_T, _P], Awaitable[_R]]) -> Callable[Concatenate[_T, _P], Coroutine[Any, Any, _R]]: ...

from . import EvilGeniusEntity as EvilGeniusEntity
from collections.abc import Awaitable as Awaitable, Callable as Callable, Coroutine
from typing import Any, Concatenate

def update_when_done(func: Callable[Concatenate[_EvilGeniusEntityT, _P], Awaitable[_R]]) -> Callable[Concatenate[_EvilGeniusEntityT, _P], Coroutine[Any, Any, _R]]: ...

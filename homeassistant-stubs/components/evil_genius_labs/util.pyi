from . import EvilGeniusEntity as EvilGeniusEntity
from collections.abc import Callable
from typing import TypeVar

CallableT = TypeVar('CallableT', bound=Callable)

def update_when_done(func: CallableT) -> CallableT: ...

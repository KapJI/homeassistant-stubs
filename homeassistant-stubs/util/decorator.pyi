from collections.abc import Callable, Hashable
from typing import TypeVar

CALLABLE_T = TypeVar('CALLABLE_T', bound=Callable)

class Registry(dict):
    def register(self, name: Hashable) -> Callable[[CALLABLE_T], CALLABLE_T]: ...

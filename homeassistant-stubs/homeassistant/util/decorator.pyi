from typing import Callable, TypeVar

CALLABLE_T = TypeVar('CALLABLE_T', bound=Callable)

class Registry(dict):
    def register(self, name: str) -> Callable[[CALLABLE_T], CALLABLE_T]: ...

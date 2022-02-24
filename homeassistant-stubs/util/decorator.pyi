from collections.abc import Callable, Hashable
from typing import Any, TypeVar

_KT = TypeVar('_KT', bound=Hashable)
_VT = TypeVar('_VT', bound=Callable[..., Any])

class Registry(dict[_KT, _VT]):
    def register(self, name: _KT) -> Callable[[_VT], _VT]: ...

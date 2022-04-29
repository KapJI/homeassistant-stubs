from _typeshed import Incomplete
from typing import Any, TypeVar

def _readonly(*args: Any, **kwargs: Any) -> Any: ...
_KT = TypeVar('_KT')
_VT = TypeVar('_VT')

class ReadOnlyDict(dict[_KT, _VT]):
    __setitem__: Incomplete
    __delitem__: Incomplete
    pop: Incomplete
    popitem: Incomplete
    clear: Incomplete
    update: Incomplete
    setdefault: Incomplete

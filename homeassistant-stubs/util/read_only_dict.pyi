from typing import Any, TypeVar

def _readonly(*args: Any, **kwargs: Any) -> Any: ...
_KT = TypeVar('_KT')
_VT = TypeVar('_VT')

class ReadOnlyDict(dict[_KT, _VT]):
    __setitem__: Any
    __delitem__: Any
    pop: Any
    popitem: Any
    clear: Any
    update: Any
    setdefault: Any

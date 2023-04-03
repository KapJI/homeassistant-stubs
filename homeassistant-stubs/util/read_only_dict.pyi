from typing import Any, TypeVar

def _readonly(*args: Any, **kwargs: Any) -> Any: ...
_KT = TypeVar('_KT')
_VT = TypeVar('_VT')

class ReadOnlyDict(dict[_KT, _VT]):
    __setitem__ = _readonly
    __delitem__ = _readonly
    pop = _readonly
    popitem = _readonly
    clear = _readonly
    update = _readonly
    setdefault = _readonly

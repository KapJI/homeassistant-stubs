from typing import Any, TypeVar

def _readonly(*args: Any, **kwargs: Any) -> Any: ...
Key = TypeVar('Key')
Value = TypeVar('Value')

class ReadOnlyDict(dict[Key, Value]):
    __setitem__: Any
    __delitem__: Any
    pop: Any
    popitem: Any
    clear: Any
    update: Any
    setdefault: Any

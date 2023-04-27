from _typeshed import Incomplete
from collections import OrderedDict
from typing import Any, TypeVar

_KT = TypeVar('_KT')
_VT = TypeVar('_VT')

class LimitedSizeDict(OrderedDict[_KT, _VT]):
    size_limit: Incomplete
    def __init__(self, *args: Any, **kwds: Any) -> None: ...
    def __setitem__(self, key: _KT, value: _VT) -> None: ...
    def _check_size_limit(self) -> None: ...

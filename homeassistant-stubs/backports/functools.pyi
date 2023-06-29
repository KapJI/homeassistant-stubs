from _typeshed import Incomplete
from collections.abc import Callable as Callable
from typing import Generic, TypeVar, overload
from typing_extensions import Self

_T = TypeVar('_T')
_R = TypeVar('_R')

class cached_property(Generic[_T, _R]):
    func: Incomplete
    attrname: Incomplete
    __doc__: Incomplete
    def __init__(self, func: Callable[[_T], _R]) -> None: ...
    def __set_name__(self, owner: type[_T], name: str) -> None: ...
    @overload
    def __get__(self, instance: None, owner: type[_T]) -> Self: ...
    @overload
    def __get__(self, instance: _T, owner: type[_T]) -> _R: ...
    __class_getitem__: Incomplete

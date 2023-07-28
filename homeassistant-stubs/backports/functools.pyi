from _typeshed import Incomplete
from collections.abc import Callable as Callable
from typing import Any, Generic, Self, TypeVar, overload

_T = TypeVar('_T')

class cached_property(Generic[_T]):
    func: Incomplete
    attrname: Incomplete
    __doc__: Incomplete
    def __init__(self, func: Callable[[Any], _T]) -> None: ...
    def __set_name__(self, owner: type[Any], name: str) -> None: ...
    @overload
    def __get__(self, instance: None, owner: type[Any] | None = ...) -> Self: ...
    @overload
    def __get__(self, instance: Any, owner: type[Any] | None = ...) -> _T: ...
    __class_getitem__: Incomplete

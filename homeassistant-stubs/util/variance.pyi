from collections.abc import Callable as Callable
from datetime import datetime, timedelta
from typing import ParamSpec, TypeVar, overload

_R = TypeVar('_R', int, float, datetime)
_P = ParamSpec('_P')

@overload
def ignore_variance(func: Callable[_P, int], ignored_variance: int) -> Callable[_P, int]: ...
@overload
def ignore_variance(func: Callable[_P, float], ignored_variance: float) -> Callable[_P, float]: ...
@overload
def ignore_variance(func: Callable[_P, datetime], ignored_variance: timedelta) -> Callable[_P, datetime]: ...

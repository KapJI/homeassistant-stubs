from collections.abc import Callable as Callable
from datetime import datetime, timedelta
from typing import TypeVar, overload

T = TypeVar('T', int, float, datetime)


@overload
def ignore_variance(func: Callable[..., int], ignored_variance: int) -> Callable[..., int]: ...
@overload
def ignore_variance(func: Callable[..., float], ignored_variance: float) -> Callable[..., float]: ...
@overload
def ignore_variance(func: Callable[..., datetime], ignored_variance: timedelta) -> Callable[..., datetime]: ...

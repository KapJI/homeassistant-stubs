from .models import WLEDEntity as WLEDEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from typing import Any, Concatenate, TypeVar

_WLEDEntityT = TypeVar('_WLEDEntityT', bound=WLEDEntity)
_P: Incomplete

def wled_exception_handler(func: Callable[Concatenate[_WLEDEntityT, _P], Coroutine[Any, Any, Any]]) -> Callable[Concatenate[_WLEDEntityT, _P], Coroutine[Any, Any, None]]: ...

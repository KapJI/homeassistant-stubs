from .entity import WLEDEntity as WLEDEntity
from collections.abc import Callable as Callable, Coroutine
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from typing import Any, Concatenate

def wled_exception_handler(func: Callable[Concatenate[_WLEDEntityT, _P], Coroutine[Any, Any, Any]]) -> Callable[Concatenate[_WLEDEntityT, _P], Coroutine[Any, Any, None]]: ...

from .const import DOMAIN as DOMAIN
from .entity import HotSpringEntity as HotSpringEntity
from collections.abc import Callable as Callable, Coroutine
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from typing import Any, Concatenate

def hotspring_exception_handler[_HotSpringEntityT: HotSpringEntity, **_P](func: Callable[Concatenate[_HotSpringEntityT, _P], Coroutine[Any, Any, Any]]) -> Callable[Concatenate[_HotSpringEntityT, _P], Coroutine[Any, Any, None]]: ...

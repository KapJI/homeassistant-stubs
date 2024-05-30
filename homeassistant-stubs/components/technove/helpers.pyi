from .entity import TechnoVEEntity as TechnoVEEntity
from collections.abc import Callable as Callable, Coroutine
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from typing import Any, Concatenate

def technove_exception_handler(func: Callable[Concatenate[_TechnoVEEntityT, _P], Coroutine[Any, Any, Any]]) -> Callable[Concatenate[_TechnoVEEntityT, _P], Coroutine[Any, Any, None]]: ...

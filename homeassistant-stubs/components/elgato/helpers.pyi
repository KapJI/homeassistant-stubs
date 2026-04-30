from .const import DOMAIN as DOMAIN
from .entity import ElgatoEntity as ElgatoEntity
from collections.abc import Callable as Callable, Coroutine
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from typing import Any, Concatenate

def elgato_exception_handler[_ElgatoEntityT: ElgatoEntity, **_P](func: Callable[Concatenate[_ElgatoEntityT, _P], Coroutine[Any, Any, Any]]) -> Callable[Concatenate[_ElgatoEntityT, _P], Coroutine[Any, Any, None]]: ...

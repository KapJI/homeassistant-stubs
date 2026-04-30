from .const import DOMAIN as DOMAIN
from .entity import FumisEntity as FumisEntity
from collections.abc import Callable as Callable, Coroutine
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from typing import Any, Concatenate

def fumis_exception_handler[_FumisEntityT: FumisEntity, **_P](func: Callable[Concatenate[_FumisEntityT, _P], Coroutine[Any, Any, Any]]) -> Callable[Concatenate[_FumisEntityT, _P], Coroutine[Any, Any, None]]: ...

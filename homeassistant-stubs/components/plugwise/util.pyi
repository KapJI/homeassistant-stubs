from .entity import PlugwiseEntity as PlugwiseEntity
from collections.abc import Awaitable as Awaitable, Callable as Callable, Coroutine
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from typing import Any, Concatenate

def plugwise_command(func: Callable[Concatenate[_PlugwiseEntityT, _P], Awaitable[_R]]) -> Callable[Concatenate[_PlugwiseEntityT, _P], Coroutine[Any, Any, _R]]: ...

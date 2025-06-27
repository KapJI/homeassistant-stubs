from .const import DOMAIN as DOMAIN
from .entity import AmazonEntity as AmazonEntity
from collections.abc import Awaitable, Callable as Callable, Coroutine
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from typing import Any, Concatenate

def alexa_api_call[_T: AmazonEntity, **_P](func: Callable[Concatenate[_T, _P], Awaitable[None]]) -> Callable[Concatenate[_T, _P], Coroutine[Any, Any, None]]: ...

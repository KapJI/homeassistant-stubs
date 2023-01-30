from .entity import RokuEntity as RokuEntity
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable, Coroutine
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from typing import Any, Concatenate, TypeVar

_RokuEntityT = TypeVar('_RokuEntityT', bound=RokuEntity)
_P: Incomplete

def format_channel_name(channel_number: str, channel_name: Union[str, None] = ...) -> str: ...
def roku_exception_handler(ignore_timeout: bool = ...) -> Callable[[Callable[Concatenate[_RokuEntityT, _P], Awaitable[Any]]], Callable[Concatenate[_RokuEntityT, _P], Coroutine[Any, Any, None]]]: ...

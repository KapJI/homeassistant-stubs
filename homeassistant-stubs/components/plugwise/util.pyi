from .entity import PlugwiseEntity as PlugwiseEntity
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable, Coroutine
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from typing import Any, Concatenate, TypeVar

_PlugwiseEntityT = TypeVar('_PlugwiseEntityT', bound=PlugwiseEntity)
_R = TypeVar('_R')
_P: Incomplete

def plugwise_command(func: Callable[Concatenate[_PlugwiseEntityT, _P], Awaitable[_R]]) -> Callable[Concatenate[_PlugwiseEntityT, _P], Coroutine[Any, Any, _R]]: ...

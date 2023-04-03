from .entity import RokuEntity as RokuEntity
from _typeshed import Incomplete
from collections.abc import Callable
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from typing import TypeVar

_RokuEntityT = TypeVar('_RokuEntityT', bound=RokuEntity)
_P: Incomplete
_FuncType: Incomplete
_ReturnFuncType: Incomplete

def format_channel_name(channel_number: str, channel_name: str | None = ...) -> str: ...
def roku_exception_handler(ignore_timeout: bool = ...) -> Callable[[_FuncType[_RokuEntityT, _P]], _ReturnFuncType[_RokuEntityT, _P]]: ...

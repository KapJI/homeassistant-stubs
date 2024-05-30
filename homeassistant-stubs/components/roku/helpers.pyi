from .entity import RokuEntity as RokuEntity
from _typeshed import Incomplete
from collections.abc import Callable
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError

_FuncType: Incomplete
_ReturnFuncType: Incomplete

def format_channel_name(channel_number: str, channel_name: str | None = None) -> str: ...
def roku_exception_handler(ignore_timeout: bool = False) -> Callable[[_FuncType[_RokuEntityT, _P]], _ReturnFuncType[_RokuEntityT, _P]]: ...

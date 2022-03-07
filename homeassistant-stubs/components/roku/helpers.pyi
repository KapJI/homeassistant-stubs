from .entity import RokuEntity as RokuEntity
from collections.abc import Awaitable as Awaitable, Callable as Callable
from typing import Any, TypeVar
from typing_extensions import Concatenate as Concatenate

_LOGGER: Any
_T = TypeVar('_T', bound=RokuEntity)
_P: Any

def format_channel_name(channel_number: str, channel_name: Union[str, None] = ...) -> str: ...
def roku_exception_handler(ignore_timeout: bool = ...) -> Callable[..., Callable]: ...

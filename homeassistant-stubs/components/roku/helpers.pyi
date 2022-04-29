from .entity import RokuEntity as RokuEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from typing import TypeVar
from typing_extensions import Concatenate as Concatenate

_LOGGER: Incomplete
_T = TypeVar('_T', bound=RokuEntity)
_P: Incomplete

def format_channel_name(channel_number: str, channel_name: Union[str, None] = ...) -> str: ...
def roku_exception_handler(ignore_timeout: bool = ...) -> Callable[..., Callable]: ...

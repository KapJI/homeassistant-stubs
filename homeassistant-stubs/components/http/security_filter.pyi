from aiohttp.web import Application as Application, Request as Request, StreamResponse as StreamResponse
from collections.abc import Callable as Callable
from homeassistant.core import callback as callback
from typing import Any, Final

_LOGGER: Any
FILTERS: Final[Any]

def setup_security_filter(app: Application) -> None: ...

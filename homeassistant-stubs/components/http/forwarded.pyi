from aiohttp.web import Application as Application, Request as Request, StreamResponse as StreamResponse
from collections.abc import Callable as Callable
from homeassistant.core import callback as callback
from typing import Any

_LOGGER: Any

def async_setup_forwarded(app: Application, use_x_forwarded_for: Union[bool, None], trusted_proxies: list[str]) -> None: ...

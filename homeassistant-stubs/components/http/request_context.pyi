from aiohttp.web import Application as Application, Request as Request, StreamResponse as StreamResponse
from collections.abc import Callable as Callable
from contextvars import ContextVar as ContextVar
from homeassistant.core import callback as callback

def setup_request_context(app: Application, context: ContextVar[Union[Request, None]]) -> None: ...

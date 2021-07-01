from aiohttp import web
from ssl import SSLContext
from typing import Any

class HomeAssistantTCPSite(web.BaseSite):
    __slots__: Any
    _host: Any
    _port: Any
    _reuse_address: Any
    _reuse_port: Any
    def __init__(self, runner: web.BaseRunner, host: Union[None, str, list[str]], port: int, *, shutdown_timeout: float = ..., ssl_context: Union[SSLContext, None] = ..., backlog: int = ..., reuse_address: Union[bool, None] = ..., reuse_port: Union[bool, None] = ...) -> None: ...
    @property
    def name(self) -> str: ...
    _server: Any
    async def start(self) -> None: ...

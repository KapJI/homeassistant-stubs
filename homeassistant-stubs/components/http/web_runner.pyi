from _typeshed import Incomplete
from aiohttp import web
from ssl import SSLContext

class HomeAssistantTCPSite(web.BaseSite):
    __slots__: Incomplete
    _host: Incomplete
    _port: Incomplete
    _reuse_address: Incomplete
    _reuse_port: Incomplete
    def __init__(self, runner: web.BaseRunner, host: None | str | list[str], port: int, *, shutdown_timeout: float = ..., ssl_context: SSLContext | None = ..., backlog: int = ..., reuse_address: bool | None = ..., reuse_port: bool | None = ...) -> None: ...
    @property
    def name(self) -> str: ...
    _server: Incomplete
    async def start(self) -> None: ...

import socket
from _typeshed import Incomplete
from aiohttp import web
from pathlib import Path
from ssl import SSLContext

class HomeAssistantTCPSite(web.BaseSite):
    __slots__: Incomplete
    _host: Incomplete
    _port: Incomplete
    _reuse_address: Incomplete
    _reuse_port: Incomplete
    def __init__(self, runner: web.BaseRunner, host: str | list[str] | None, port: int, *, ssl_context: SSLContext | None = None, backlog: int = 128, reuse_address: bool | None = None, reuse_port: bool | None = None) -> None: ...
    @property
    def name(self) -> str: ...
    _server: Incomplete
    async def start(self) -> None: ...

class HomeAssistantUnixSite(web.BaseSite):
    __slots__: Incomplete
    _path: Incomplete
    def __init__(self, runner: web.BaseRunner, path: Path, *, backlog: int = 128) -> None: ...
    @property
    def name(self) -> str: ...
    def _create_unix_socket(self) -> socket.socket: ...
    _server: Incomplete
    async def start(self) -> None: ...

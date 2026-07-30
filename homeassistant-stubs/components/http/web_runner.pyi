import socket
from _typeshed import Incomplete
from aiohttp import web
from pathlib import Path
from typing import override

class HomeAssistantUnixSite(web.BaseSite):
    __slots__: Incomplete
    _path: Incomplete
    def __init__(self, runner: web.BaseRunner, path: Path, *, backlog: int = 128) -> None: ...
    @property
    @override
    def name(self) -> str: ...
    def _create_unix_socket(self) -> socket.socket: ...
    _server: Incomplete
    @override
    async def start(self) -> None: ...

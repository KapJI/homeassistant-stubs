from .json import json_loads as json_loads
from _typeshed import Incomplete
from aiohttp import web as web
from aiohttp.typedefs import JSONDecoder as JSONDecoder
from multidict import CIMultiDict, MultiDict
from typing import Any

class MockStreamReader:
    _content: Incomplete
    def __init__(self, content: bytes) -> None: ...
    async def read(self, byte_count: int = -1) -> bytes: ...

class MockStreamReaderChunked(MockStreamReader):
    async def readchunk(self) -> tuple[bytes, bool]: ...

class MockPayloadWriter:
    def enable_chunking(self) -> None: ...
    def send_headers(self, *args: Any, **kwargs: Any) -> None: ...
    async def write_headers(self, *args: Any, **kwargs: Any) -> None: ...
    async def write(self, *args: Any, **kwargs: Any) -> None: ...

_MOCK_PAYLOAD_WRITER: Incomplete

class MockRequest:
    mock_source: str | None
    method: Incomplete
    url: Incomplete
    status: Incomplete
    headers: CIMultiDict[str]
    query_string: Incomplete
    keep_alive: bool
    version: Incomplete
    _content: Incomplete
    _payload_writer: Incomplete
    def __init__(self, content: bytes, mock_source: str, method: str = 'GET', status: int = ..., headers: dict[str, str] | None = None, query_string: str | None = None, url: str = '') -> None: ...
    async def _prepare_hook(self, response: Any) -> None: ...
    @property
    def query(self) -> MultiDict[str]: ...
    @property
    def _text(self) -> str: ...
    @property
    def content(self) -> MockStreamReader: ...
    @property
    def body_exists(self) -> bool: ...
    async def json(self, loads: JSONDecoder = ...) -> Any: ...
    async def post(self) -> MultiDict[str]: ...
    async def text(self) -> str: ...

def serialize_response(response: web.Response) -> dict[str, Any]: ...

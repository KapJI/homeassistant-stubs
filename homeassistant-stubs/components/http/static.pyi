from _typeshed import Incomplete
from aiohttp.web import Request as Request, StreamResponse as StreamResponse
from aiohttp.web_urldispatcher import StaticResource
from collections.abc import Mapping
from typing import Final

CACHE_TIME: Final[Incomplete]
CACHE_HEADERS: Final[Mapping[str, str]]

class CachingStaticResource(StaticResource):
    async def _handle(self, request: Request) -> StreamResponse: ...

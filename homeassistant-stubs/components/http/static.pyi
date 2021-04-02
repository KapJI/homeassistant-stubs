from aiohttp.web_urldispatcher import StaticResource
from typing import Any

CACHE_TIME: Any
CACHE_HEADERS: Any

class CachingStaticResource(StaticResource):
    async def _handle(self, request: Any): ...

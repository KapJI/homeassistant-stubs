from .const import KEY_HASS as KEY_HASS
from _typeshed import Incomplete
from aiohttp.web import Request as Request, StreamResponse as StreamResponse
from aiohttp.web_urldispatcher import StaticResource
from collections.abc import Mapping, MutableMapping
from homeassistant.core import HomeAssistant as HomeAssistant
from pathlib import Path
from typing import Final

CACHE_TIME: Final[Incomplete]
CACHE_HEADER: Incomplete
CACHE_HEADERS: Mapping[str, str]
PATH_CACHE: MutableMapping[tuple[str, Path, bool], tuple[Path | None, str | None]]

def _get_file_path(rel_url: str, directory: Path, follow_symlinks: bool) -> Path | None: ...

class CachingStaticResource(StaticResource):
    async def _handle(self, request: Request) -> StreamResponse: ...

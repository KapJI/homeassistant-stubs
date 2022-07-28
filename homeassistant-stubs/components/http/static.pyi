from .const import KEY_HASS as KEY_HASS
from _typeshed import Incomplete
from aiohttp.web import Request as Request, StreamResponse as StreamResponse
from aiohttp.web_urldispatcher import StaticResource
from collections.abc import Mapping
from homeassistant.core import HomeAssistant as HomeAssistant
from pathlib import Path
from typing import Final

CACHE_TIME: Final[Incomplete]
CACHE_HEADERS: Final[Mapping[str, str]]
PATH_CACHE: Incomplete

def _get_file_path(filename: Union[str, Path], directory: Path, follow_symlinks: bool) -> Union[Path, None]: ...

class CachingStaticResource(StaticResource):
    async def _handle(self, request: Request) -> StreamResponse: ...

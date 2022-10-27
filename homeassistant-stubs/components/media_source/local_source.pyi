from .const import DOMAIN as DOMAIN, MEDIA_CLASS_MAP as MEDIA_CLASS_MAP, MEDIA_MIME_TYPES as MEDIA_MIME_TYPES
from .error import Unresolvable as Unresolvable
from .models import BrowseMediaSource as BrowseMediaSource, MediaSource as MediaSource, MediaSourceItem as MediaSourceItem, PlayMedia as PlayMedia
from _typeshed import Incomplete
from aiohttp import web
from aiohttp.web_request import FileField
from homeassistant.components import http as http, websocket_api as websocket_api
from homeassistant.components.media_player import BrowseError as BrowseError, MediaClass as MediaClass
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import Unauthorized as Unauthorized
from homeassistant.util import raise_if_invalid_filename as raise_if_invalid_filename, raise_if_invalid_path as raise_if_invalid_path
from pathlib import Path
from typing import Any

MAX_UPLOAD_SIZE: Incomplete
LOGGER: Incomplete

def async_setup(hass: HomeAssistant) -> None: ...

class LocalSource(MediaSource):
    name: str
    hass: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    def async_full_path(self, source_dir_id: str, location: str) -> Path: ...
    def async_parse_identifier(self, item: MediaSourceItem) -> tuple[str, str]: ...
    async def async_resolve_media(self, item: MediaSourceItem) -> PlayMedia: ...
    async def async_browse_media(self, item: MediaSourceItem) -> BrowseMediaSource: ...
    def _browse_media(self, source_dir_id: Union[str, None], location: str) -> BrowseMediaSource: ...
    def _build_item_response(self, source_dir_id: str, path: Path, is_child: bool = ...) -> Union[BrowseMediaSource, None]: ...

class LocalMediaView(http.HomeAssistantView):
    url: str
    name: str
    hass: Incomplete
    source: Incomplete
    def __init__(self, hass: HomeAssistant, source: LocalSource) -> None: ...
    async def get(self, request: web.Request, source_dir_id: str, location: str) -> web.FileResponse: ...

class UploadMediaView(http.HomeAssistantView):
    url: str
    name: str
    hass: Incomplete
    source: Incomplete
    schema: Incomplete
    def __init__(self, hass: HomeAssistant, source: LocalSource) -> None: ...
    async def post(self, request: web.Request) -> web.Response: ...
    def _move_file(self, target_dir: Path, uploaded_file: FileField) -> None: ...

async def websocket_remove_media(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...

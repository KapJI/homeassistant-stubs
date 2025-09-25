import io
from .const import DOMAIN as DOMAIN, MEDIA_CLASS_MAP as MEDIA_CLASS_MAP, MEDIA_MIME_TYPES as MEDIA_MIME_TYPES, MEDIA_SOURCE_DATA as MEDIA_SOURCE_DATA
from .error import Unresolvable as Unresolvable
from .models import BrowseMediaSource as BrowseMediaSource, MediaSource as MediaSource, MediaSourceItem as MediaSourceItem, PlayMedia as PlayMedia
from _typeshed import Incomplete
from aiohttp import web
from homeassistant.components import http as http, websocket_api as websocket_api
from homeassistant.components.http import require_admin as require_admin
from homeassistant.components.media_player import BrowseError as BrowseError, MediaClass as MediaClass
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.util import raise_if_invalid_filename as raise_if_invalid_filename, raise_if_invalid_path as raise_if_invalid_path
from pathlib import Path
from typing import Any, Protocol

MAX_UPLOAD_SIZE: Incomplete
LOGGER: Incomplete

class PathNotSupportedError(HomeAssistantError): ...
class InvalidFileNameError(HomeAssistantError): ...

class UploadedFile(Protocol):
    filename: str
    file: io.IOBase
    content_type: str

async def async_get_media_source(hass: HomeAssistant) -> LocalSource: ...

class LocalSource(MediaSource):
    hass: Incomplete
    name: Incomplete
    media_dirs: Incomplete
    url_prefix: Incomplete
    def __init__(self, hass: HomeAssistant, domain: str, name: str, media_dirs: dict[str, str], url_prefix: str) -> None: ...
    @callback
    def async_full_path(self, source_dir_id: str, location: str) -> Path: ...
    @callback
    def async_parse_identifier(self, item: MediaSourceItem) -> tuple[str, str]: ...
    async def async_delete_media(self, item: MediaSourceItem) -> None: ...
    async def async_upload_media(self, target_folder: MediaSourceItem, uploaded_file: UploadedFile) -> str: ...
    async def async_resolve_media(self, item: MediaSourceItem) -> PlayMedia: ...
    async def async_browse_media(self, item: MediaSourceItem) -> BrowseMediaSource: ...
    def _browse_media(self, source_dir_id: str | None, location: str) -> BrowseMediaSource: ...
    def _build_item_response(self, source_dir_id: str, path: Path, is_child: bool = False) -> BrowseMediaSource | None: ...

class LocalMediaView(http.HomeAssistantView):
    name: str
    hass: Incomplete
    source: Incomplete
    url: Incomplete
    def __init__(self, hass: HomeAssistant, source: LocalSource) -> None: ...
    async def _validate_media_path(self, source_dir_id: str, location: str) -> Path: ...
    async def head(self, request: web.Request, source_dir_id: str, location: str) -> None: ...
    async def get(self, request: web.Request, source_dir_id: str, location: str) -> web.FileResponse: ...

class UploadMediaView(http.HomeAssistantView):
    url: str
    name: str
    schema: Incomplete
    @require_admin
    async def post(self, request: web.Request) -> web.Response: ...

@websocket_api.require_admin
@websocket_api.async_response
async def websocket_remove_media(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...

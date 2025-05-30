from .const import DOMAIN as DOMAIN
from .coordinator import ImmichConfigEntry as ImmichConfigEntry
from _typeshed import Incomplete
from aiohttp.web import Request as Request, Response, StreamResponse
from homeassistant.components.http import HomeAssistantView as HomeAssistantView
from homeassistant.components.media_player import MediaClass as MediaClass
from homeassistant.components.media_source import BrowseError as BrowseError, BrowseMediaSource as BrowseMediaSource, MediaSource as MediaSource, MediaSourceItem as MediaSourceItem, PlayMedia as PlayMedia, Unresolvable as Unresolvable
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import ChunkAsyncStreamIterator as ChunkAsyncStreamIterator

LOGGER: Incomplete

async def async_get_media_source(hass: HomeAssistant) -> MediaSource: ...

class ImmichMediaSourceIdentifier:
    unique_id: Incomplete
    collection: Incomplete
    collection_id: Incomplete
    asset_id: Incomplete
    file_name: Incomplete
    mime_type: Incomplete
    def __init__(self, identifier: str) -> None: ...

class ImmichMediaSource(MediaSource):
    name: str
    hass: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    async def async_browse_media(self, item: MediaSourceItem) -> BrowseMediaSource: ...
    async def _async_build_immich(self, item: MediaSourceItem, entries: list[ConfigEntry]) -> list[BrowseMediaSource]: ...
    async def async_resolve_media(self, item: MediaSourceItem) -> PlayMedia: ...

class ImmichMediaView(HomeAssistantView):
    url: str
    name: str
    hass: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    async def get(self, request: Request, source_dir_id: str, location: str) -> Response | StreamResponse: ...

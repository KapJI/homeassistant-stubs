from .const import DOMAIN as DOMAIN
from .coordinator import ImmichConfigEntry as ImmichConfigEntry
from _typeshed import Incomplete
from aiohttp.web import Request as Request, Response, StreamResponse
from aioimmich.assets.models import AssetType, ImmichAsset as ImmichAsset
from homeassistant.components.http import HomeAssistantView as HomeAssistantView
from homeassistant.components.media_player import BrowseError as BrowseError, MediaClass as MediaClass, SearchMedia as SearchMedia, SearchMediaQuery as SearchMediaQuery
from homeassistant.components.media_source import BrowseMediaSource as BrowseMediaSource, MediaSource as MediaSource, MediaSourceItem as MediaSourceItem, PlayMedia as PlayMedia, Unresolvable as Unresolvable
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import ChunkAsyncStreamIterator as ChunkAsyncStreamIterator
from typing import TypedDict, override

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

class ImmichSmartSearchArgs(TypedDict, total=False):
    query: str
    page_size: int
    max_pages: int
    asset_type: AssetType
    album_ids: list[str]
    person_ids: list[str]
    tag_ids: list[str]
    is_favorite: bool
    is_not_in_album: bool

MEDIA_CLASS_ASSET_TYPE_MAPPING: Incomplete

def _parse_assets(assets: list[ImmichAsset], identifier: ImmichMediaSourceIdentifier) -> list[BrowseMediaSource]: ...

class ImmichMediaSource(MediaSource):
    name: str
    hass: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    @override
    async def async_browse_media(self, item: MediaSourceItem) -> BrowseMediaSource: ...
    async def _async_build_immich(self, item: MediaSourceItem, entries: list[ConfigEntry]) -> tuple[str, list[BrowseMediaSource]]: ...
    @override
    async def async_resolve_media(self, item: MediaSourceItem) -> PlayMedia: ...
    @override
    async def async_search_media(self, item: MediaSourceItem, query: SearchMediaQuery) -> SearchMedia: ...

class ImmichMediaView(HomeAssistantView):
    url: str
    name: str
    hass: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    async def get(self, request: Request, source_dir_id: str, location: str) -> Response | StreamResponse: ...

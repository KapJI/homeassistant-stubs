from .const import DATA_LOCAL_SOURCE as DATA_LOCAL_SOURCE, DATA_MEDIA_SOURCE_PLATFORMS as DATA_MEDIA_SOURCE_PLATFORMS, DOMAIN as DOMAIN, URI_SCHEME as URI_SCHEME, URI_SCHEME_REGEX as URI_SCHEME_REGEX
from _typeshed import Incomplete
from dataclasses import dataclass, field
from homeassistant.components.media_player import BrowseMedia as BrowseMedia, MediaClass as MediaClass, MediaType as MediaType, SearchMedia as SearchMedia, SearchMediaQuery as SearchMediaQuery
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.translation import async_get_cached_translations as async_get_cached_translations
from pathlib import Path
from typing import Any

async def _async_get_media_sources(hass: HomeAssistant) -> dict[str, MediaSource]: ...
async def _async_get_media_source(hass: HomeAssistant, domain: str) -> MediaSource | None: ...

@dataclass(slots=True)
class PlayMedia:
    url: str
    mime_type: str
    path: Path | None = field(kw_only=True, default=None)

class BrowseMediaSource(BrowseMedia):
    domain: Incomplete
    identifier: Incomplete
    def __init__(self, *, domain: str, identifier: str | None, **kwargs: Any) -> None: ...

class RootBrowseMediaSource(BrowseMedia):
    domain: None
    identifier: None
    def __init__(self, **kwargs: Any) -> None: ...

@dataclass(slots=True)
class MediaSourceItem:
    hass: HomeAssistant
    domain: str | None
    identifier: str
    target_media_player: str | None
    @property
    def media_source_id(self) -> str: ...
    async def async_browse(self) -> BrowseMediaSource | RootBrowseMediaSource: ...
    async def async_search(self, query: SearchMediaQuery) -> SearchMedia: ...
    async def async_resolve(self) -> PlayMedia: ...
    async def _async_media_source(self) -> MediaSource: ...
    @classmethod
    def from_uri(cls, hass: HomeAssistant, uri: str, target_media_player: str | None) -> MediaSourceItem: ...

class MediaSource:
    name: str | None
    domain: Incomplete
    def __init__(self, domain: str) -> None: ...
    async def async_resolve_media(self, item: MediaSourceItem) -> PlayMedia: ...
    async def async_browse_media(self, item: MediaSourceItem) -> BrowseMediaSource: ...
    async def async_search_media(self, item: MediaSourceItem, query: SearchMediaQuery) -> SearchMedia: ...

from .const import DOMAIN as DOMAIN, URI_SCHEME as URI_SCHEME, URI_SCHEME_REGEX as URI_SCHEME_REGEX
from _typeshed import Incomplete
from abc import ABC
from homeassistant.components.media_player import BrowseMedia as BrowseMedia
from homeassistant.components.media_player.const import MEDIA_CLASS_APP as MEDIA_CLASS_APP, MEDIA_TYPE_APP as MEDIA_TYPE_APP, MEDIA_TYPE_APPS as MEDIA_TYPE_APPS
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from typing import Any

class PlayMedia:
    url: str
    mime_type: str
    def __init__(self, url, mime_type) -> None: ...

class BrowseMediaSource(BrowseMedia):
    children: Union[list[Union[BrowseMediaSource, BrowseMedia]], None]
    domain: Incomplete
    identifier: Incomplete
    def __init__(self, *, domain: Union[str, None], identifier: Union[str, None], **kwargs: Any) -> None: ...

class MediaSourceItem:
    hass: HomeAssistant
    domain: Union[str, None]
    identifier: str
    target_media_player: Union[str, None]
    async def async_browse(self) -> BrowseMediaSource: ...
    async def async_resolve(self) -> PlayMedia: ...
    def async_media_source(self) -> MediaSource: ...
    @classmethod
    def from_uri(cls, hass: HomeAssistant, uri: str, target_media_player: Union[str, None]) -> MediaSourceItem: ...
    def __init__(self, hass, domain, identifier, target_media_player) -> None: ...

class MediaSource(ABC):
    name: Union[str, None]
    domain: Incomplete
    def __init__(self, domain: str) -> None: ...
    async def async_resolve_media(self, item: MediaSourceItem) -> PlayMedia: ...
    async def async_browse_media(self, item: MediaSourceItem) -> BrowseMediaSource: ...

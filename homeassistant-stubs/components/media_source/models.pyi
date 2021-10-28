from .const import DOMAIN as DOMAIN, URI_SCHEME as URI_SCHEME, URI_SCHEME_REGEX as URI_SCHEME_REGEX
from abc import ABC
from homeassistant.components.media_player import BrowseMedia as BrowseMedia
from homeassistant.components.media_player.const import MEDIA_CLASS_CHANNEL as MEDIA_CLASS_CHANNEL, MEDIA_CLASS_DIRECTORY as MEDIA_CLASS_DIRECTORY, MEDIA_TYPE_CHANNEL as MEDIA_TYPE_CHANNEL, MEDIA_TYPE_CHANNELS as MEDIA_TYPE_CHANNELS
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from typing import Any

class PlayMedia:
    url: str
    mime_type: str

class BrowseMediaSource(BrowseMedia):
    children: Union[list[Union[BrowseMediaSource, BrowseMedia]], None]
    domain: Any
    identifier: Any
    def __init__(self, domain: Union[str, None], identifier: Union[str, None], **kwargs: Any) -> None: ...

class MediaSourceItem:
    hass: HomeAssistant
    domain: Union[str, None]
    identifier: str
    async def async_browse(self) -> BrowseMediaSource: ...
    async def async_resolve(self) -> PlayMedia: ...
    def async_media_source(self) -> MediaSource: ...
    @classmethod
    def from_uri(cls, hass: HomeAssistant, uri: str) -> MediaSourceItem: ...

class MediaSource(ABC):
    name: Union[str, None]
    domain: Any
    def __init__(self, domain: str) -> None: ...
    async def async_resolve_media(self, item: MediaSourceItem) -> PlayMedia: ...
    async def async_browse_media(self, item: MediaSourceItem) -> BrowseMediaSource: ...

from . import Camera as Camera, _async_stream_endpoint_url as _async_stream_endpoint_url
from .const import DOMAIN as DOMAIN, STREAM_TYPE_HLS as STREAM_TYPE_HLS
from homeassistant.components.media_player.const import MEDIA_CLASS_APP as MEDIA_CLASS_APP, MEDIA_CLASS_VIDEO as MEDIA_CLASS_VIDEO
from homeassistant.components.media_player.errors import BrowseError as BrowseError
from homeassistant.components.media_source.error import Unresolvable as Unresolvable
from homeassistant.components.media_source.models import BrowseMediaSource as BrowseMediaSource, MediaSource as MediaSource, MediaSourceItem as MediaSourceItem, PlayMedia as PlayMedia
from homeassistant.components.stream.const import FORMAT_CONTENT_TYPE as FORMAT_CONTENT_TYPE, HLS_PROVIDER as HLS_PROVIDER
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from typing import Any

async def async_get_media_source(hass: HomeAssistant) -> CameraMediaSource: ...

class CameraMediaSource(MediaSource):
    name: str
    hass: Any
    def __init__(self, hass: HomeAssistant) -> None: ...
    async def async_resolve_media(self, item: MediaSourceItem) -> PlayMedia: ...
    async def async_browse_media(self, item: MediaSourceItem) -> BrowseMediaSource: ...

from collections.abc import Mapping
from google_nest_sdm.device import Device as Device
from google_nest_sdm.event import ImageEventBase as ImageEventBase
from homeassistant.components.media_player.const import MEDIA_CLASS_DIRECTORY as MEDIA_CLASS_DIRECTORY, MEDIA_CLASS_IMAGE as MEDIA_CLASS_IMAGE, MEDIA_CLASS_VIDEO as MEDIA_CLASS_VIDEO, MEDIA_TYPE_IMAGE as MEDIA_TYPE_IMAGE, MEDIA_TYPE_VIDEO as MEDIA_TYPE_VIDEO
from homeassistant.components.media_player.errors import BrowseError as BrowseError
from homeassistant.components.media_source.error import Unresolvable as Unresolvable
from homeassistant.components.media_source.models import BrowseMediaSource as BrowseMediaSource, MediaSource as MediaSource, MediaSourceItem as MediaSourceItem, PlayMedia as PlayMedia
from homeassistant.components.nest.const import DATA_SUBSCRIBER as DATA_SUBSCRIBER, DOMAIN as DOMAIN
from homeassistant.components.nest.device_info import NestDeviceInfo as NestDeviceInfo
from homeassistant.components.nest.events import MEDIA_SOURCE_EVENT_TITLE_MAP as MEDIA_SOURCE_EVENT_TITLE_MAP
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.template import DATE_STR_FORMAT as DATE_STR_FORMAT
from typing import Any

_LOGGER: Any
MEDIA_SOURCE_TITLE: str
DEVICE_TITLE_FORMAT: str
CLIP_TITLE_FORMAT: str
EVENT_MEDIA_API_URL_FORMAT: str

async def async_get_media_source(hass: HomeAssistant) -> MediaSource: ...
async def get_media_source_devices(hass: HomeAssistant) -> Mapping[str, Device]: ...

class MediaId:
    device_id: str
    event_id: Union[str, None]
    @property
    def identifier(self) -> str: ...

def parse_media_id(identifier: Union[str, None] = ...) -> Union[MediaId, None]: ...

class NestMediaSource(MediaSource):
    name: str
    hass: Any
    def __init__(self, hass: HomeAssistant) -> None: ...
    async def async_resolve_media(self, item: MediaSourceItem) -> PlayMedia: ...
    async def async_browse_media(self, item: MediaSourceItem) -> BrowseMediaSource: ...
    async def devices(self) -> Mapping[str, Device]: ...

async def _get_events(device: Device) -> Mapping[str, ImageEventBase]: ...
def _browse_root() -> BrowseMediaSource: ...
def _browse_device(device_id: MediaId, device: Device) -> BrowseMediaSource: ...
def _browse_event(event_id: MediaId, device: Device, event: ImageEventBase) -> BrowseMediaSource: ...

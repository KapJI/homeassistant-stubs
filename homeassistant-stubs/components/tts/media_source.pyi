from . import SpeechManager as SpeechManager
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.media_player import BrowseError as BrowseError, MediaClass as MediaClass
from homeassistant.components.media_source import BrowseMediaSource as BrowseMediaSource, MediaSource as MediaSource, MediaSourceItem as MediaSourceItem, PlayMedia as PlayMedia, Unresolvable as Unresolvable
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.network import get_url as get_url
from typing import TypedDict

async def async_get_media_source(hass: HomeAssistant) -> TTSMediaSource: ...
def generate_media_source_id(hass: HomeAssistant, message: str, engine: Union[str, None] = ..., language: Union[str, None] = ..., options: Union[dict, None] = ..., cache: Union[bool, None] = ...) -> str: ...

class MediaSourceOptions(TypedDict):
    engine: str
    message: str
    language: Union[str, None]
    options: Union[dict, None]
    cache: Union[bool, None]

def media_source_id_to_kwargs(media_source_id: str) -> MediaSourceOptions: ...

class TTSMediaSource(MediaSource):
    name: str
    hass: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    async def async_resolve_media(self, item: MediaSourceItem) -> PlayMedia: ...
    async def async_browse_media(self, item: MediaSourceItem) -> BrowseMediaSource: ...
    def _provider_item(self, provider_domain: str, params: Union[str, None] = ...) -> BrowseMediaSource: ...

from . import SpeechManager as SpeechManager, TextToSpeechEntity as TextToSpeechEntity
from .const import DATA_TTS_MANAGER as DATA_TTS_MANAGER, DOMAIN as DOMAIN
from .helper import get_engine_instance as get_engine_instance
from _typeshed import Incomplete
from homeassistant.components.media_player import BrowseError as BrowseError, MediaClass as MediaClass
from homeassistant.components.media_source import BrowseMediaSource as BrowseMediaSource, MediaSource as MediaSource, MediaSourceItem as MediaSourceItem, PlayMedia as PlayMedia, Unresolvable as Unresolvable
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from typing import TypedDict

async def async_get_media_source(hass: HomeAssistant) -> TTSMediaSource: ...
def generate_media_source_id(hass: HomeAssistant, message: str, engine: str | None = ..., language: str | None = ..., options: dict | None = ..., cache: bool | None = ...) -> str: ...

class MediaSourceOptions(TypedDict):
    engine: str
    message: str
    language: str | None
    options: dict | None
    cache: bool | None

def media_source_id_to_kwargs(media_source_id: str) -> MediaSourceOptions: ...

class TTSMediaSource(MediaSource):
    name: str
    hass: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    async def async_resolve_media(self, item: MediaSourceItem) -> PlayMedia: ...
    async def async_browse_media(self, item: MediaSourceItem) -> BrowseMediaSource: ...
    def _engine_item(self, engine: str, params: str | None = ...) -> BrowseMediaSource: ...

from . import SpeechManager as SpeechManager
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.media_player.const import MEDIA_CLASS_APP as MEDIA_CLASS_APP
from homeassistant.components.media_player.errors import BrowseError as BrowseError
from homeassistant.components.media_source.error import Unresolvable as Unresolvable
from homeassistant.components.media_source.models import BrowseMediaSource as BrowseMediaSource, MediaSource as MediaSource, MediaSourceItem as MediaSourceItem, PlayMedia as PlayMedia
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.network import get_url as get_url

async def async_get_media_source(hass: HomeAssistant) -> TTSMediaSource: ...

class TTSMediaSource(MediaSource):
    name: str
    hass: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    async def async_resolve_media(self, item: MediaSourceItem) -> PlayMedia: ...
    async def async_browse_media(self, item: MediaSourceItem) -> BrowseMediaSource: ...
    def _provider_item(self, provider_domain: str, params: Union[str, None] = ...) -> BrowseMediaSource: ...

from . import ImageEntity as ImageEntity
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.media_player import BrowseError as BrowseError, MediaClass as MediaClass
from homeassistant.components.media_source.error import Unresolvable as Unresolvable
from homeassistant.components.media_source.models import BrowseMediaSource as BrowseMediaSource, MediaSource as MediaSource, MediaSourceItem as MediaSourceItem, PlayMedia as PlayMedia
from homeassistant.const import ATTR_FRIENDLY_NAME as ATTR_FRIENDLY_NAME
from homeassistant.core import HomeAssistant as HomeAssistant, State as State
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent

async def async_get_media_source(hass: HomeAssistant) -> ImageMediaSource: ...

class ImageMediaSource(MediaSource):
    name: str
    hass: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    async def async_resolve_media(self, item: MediaSourceItem) -> PlayMedia: ...
    async def async_browse_media(self, item: MediaSourceItem) -> BrowseMediaSource: ...

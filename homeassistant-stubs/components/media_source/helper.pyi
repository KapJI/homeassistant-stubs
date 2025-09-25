from .const import DOMAIN as DOMAIN, MEDIA_SOURCE_DATA as MEDIA_SOURCE_DATA
from .error import UnknownMediaSource as UnknownMediaSource, Unresolvable as Unresolvable
from .models import BrowseMediaSource as BrowseMediaSource, MediaSourceItem as MediaSourceItem, PlayMedia as PlayMedia
from collections.abc import Callable as Callable
from homeassistant.components.media_player import BrowseError as BrowseError, BrowseMedia as BrowseMedia
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.frame import report_usage as report_usage
from homeassistant.helpers.typing import UNDEFINED as UNDEFINED, UndefinedType as UndefinedType
from homeassistant.loader import bind_hass as bind_hass

@callback
def _get_media_item(hass: HomeAssistant, media_content_id: str | None, target_media_player: str | None) -> MediaSourceItem: ...
@bind_hass
async def async_browse_media(hass: HomeAssistant, media_content_id: str | None, *, content_filter: Callable[[BrowseMedia], bool] | None = None) -> BrowseMediaSource: ...
@bind_hass
async def async_resolve_media(hass: HomeAssistant, media_content_id: str, target_media_player: str | None | UndefinedType = ...) -> PlayMedia: ...

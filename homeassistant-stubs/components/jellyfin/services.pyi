from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.media_player import ATTR_MEDIA as ATTR_MEDIA, ATTR_MEDIA_CONTENT_ID as ATTR_MEDIA_CONTENT_ID, MediaPlayerEntityFeature as MediaPlayerEntityFeature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import service as service
from typing import Any

JELLYFIN_PLAY_MEDIA_SHUFFLE_SCHEMA: Incomplete

def _promote_media_fields(data: dict[str, Any]) -> dict[str, Any]: ...
async def async_setup_services(hass: HomeAssistant) -> None: ...

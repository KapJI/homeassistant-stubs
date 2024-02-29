from . import ATTR_MEDIA_VOLUME_LEVEL as ATTR_MEDIA_VOLUME_LEVEL, DOMAIN as DOMAIN
from homeassistant.const import SERVICE_MEDIA_NEXT_TRACK as SERVICE_MEDIA_NEXT_TRACK, SERVICE_MEDIA_PAUSE as SERVICE_MEDIA_PAUSE, SERVICE_MEDIA_PLAY as SERVICE_MEDIA_PLAY, SERVICE_VOLUME_SET as SERVICE_VOLUME_SET
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import intent as intent

INTENT_MEDIA_PAUSE: str
INTENT_MEDIA_UNPAUSE: str
INTENT_MEDIA_NEXT: str
INTENT_SET_VOLUME: str

async def async_setup_intents(hass: HomeAssistant) -> None: ...

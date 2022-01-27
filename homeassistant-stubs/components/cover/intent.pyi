from . import DOMAIN as DOMAIN
from homeassistant.const import SERVICE_CLOSE_COVER as SERVICE_CLOSE_COVER, SERVICE_OPEN_COVER as SERVICE_OPEN_COVER
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import intent as intent

INTENT_OPEN_COVER: str
INTENT_CLOSE_COVER: str

async def async_setup_intents(hass: HomeAssistant) -> None: ...

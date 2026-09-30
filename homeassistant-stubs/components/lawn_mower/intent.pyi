from . import LawnMowerEntityFeature as LawnMowerEntityFeature, SERVICE_DOCK as SERVICE_DOCK, SERVICE_START_MOWING as SERVICE_START_MOWING
from .const import DOMAIN as DOMAIN
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import intent as intent

INTENT_LANW_MOWER_START_MOWING: str
INTENT_LANW_MOWER_DOCK: str

async def async_setup_intents(hass: HomeAssistant) -> None: ...

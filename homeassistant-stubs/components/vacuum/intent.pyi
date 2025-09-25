from . import DOMAIN as DOMAIN, SERVICE_RETURN_TO_BASE as SERVICE_RETURN_TO_BASE, SERVICE_START as SERVICE_START, VacuumEntityFeature as VacuumEntityFeature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import intent as intent

INTENT_VACUUM_START: str
INTENT_VACUUM_RETURN_TO_BASE: str

async def async_setup_intents(hass: HomeAssistant) -> None: ...

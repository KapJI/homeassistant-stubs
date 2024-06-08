from . import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import intent as intent

INTENT_GET_TEMPERATURE: str

async def async_setup_intents(hass: HomeAssistant) -> None: ...

class GetTemperatureIntent(intent.IntentHandler):
    intent_type = INTENT_GET_TEMPERATURE
    description: str
    slot_schema: Incomplete
    platforms: Incomplete
    async def async_handle(self, intent_obj: intent.Intent) -> intent.IntentResponse: ...

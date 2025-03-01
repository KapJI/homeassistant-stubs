from . import ATTR_TEMPERATURE as ATTR_TEMPERATURE, ClimateEntityFeature as ClimateEntityFeature, DOMAIN as DOMAIN, INTENT_SET_TEMPERATURE as INTENT_SET_TEMPERATURE, SERVICE_SET_TEMPERATURE as SERVICE_SET_TEMPERATURE
from _typeshed import Incomplete
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import intent as intent

async def async_setup_intents(hass: HomeAssistant) -> None: ...

class SetTemperatureIntent(intent.IntentHandler):
    intent_type = INTENT_SET_TEMPERATURE
    description: str
    slot_schema: Incomplete
    platforms: Incomplete
    async def async_handle(self, intent_obj: intent.Intent) -> intent.IntentResponse: ...

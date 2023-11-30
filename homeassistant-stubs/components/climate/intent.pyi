from . import ClimateEntity as ClimateEntity, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant, State as State
from homeassistant.helpers import intent as intent
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent

INTENT_GET_TEMPERATURE: str

async def async_setup_intents(hass: HomeAssistant) -> None: ...

class GetTemperatureIntent(intent.IntentHandler):
    intent_type = INTENT_GET_TEMPERATURE
    slot_schema: Incomplete
    async def async_handle(self, intent_obj: intent.Intent) -> intent.IntentResponse: ...

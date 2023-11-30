from . import DOMAIN as DOMAIN, WeatherEntity as WeatherEntity
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant, State as State
from homeassistant.helpers import intent as intent
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent

INTENT_GET_WEATHER: str

async def async_setup_intents(hass: HomeAssistant) -> None: ...

class GetWeatherIntent(intent.IntentHandler):
    intent_type = INTENT_GET_WEATHER
    slot_schema: Incomplete
    async def async_handle(self, intent_obj: intent.Intent) -> intent.IntentResponse: ...

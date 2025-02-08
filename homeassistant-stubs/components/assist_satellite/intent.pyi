from .const import AssistSatelliteEntityFeature as AssistSatelliteEntityFeature, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import intent as intent
from typing import Final

EXCLUDED_DOMAINS: Final[set[str]]

async def async_setup_intents(hass: HomeAssistant) -> None: ...

class BroadcastIntentHandler(intent.IntentHandler):
    intent_type: Incomplete
    description: str
    @property
    def slot_schema(self) -> dict | None: ...
    async def async_handle(self, intent_obj: intent.Intent) -> intent.IntentResponse: ...

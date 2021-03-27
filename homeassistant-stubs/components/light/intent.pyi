from . import ATTR_BRIGHTNESS_PCT as ATTR_BRIGHTNESS_PCT, ATTR_RGB_COLOR as ATTR_RGB_COLOR, DOMAIN as DOMAIN, SERVICE_TURN_ON as SERVICE_TURN_ON, SUPPORT_BRIGHTNESS as SUPPORT_BRIGHTNESS, SUPPORT_COLOR as SUPPORT_COLOR
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import intent as intent
from typing import Any

INTENT_SET: str

async def async_setup_intents(hass: HomeAssistant) -> None: ...

class SetIntentHandler(intent.IntentHandler):
    intent_type: Any = ...
    slot_schema: Any = ...
    async def async_handle(self, intent_obj: intent.Intent) -> intent.IntentResponse: ...

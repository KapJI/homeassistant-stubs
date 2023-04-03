from . import ATTR_BRIGHTNESS_PCT as ATTR_BRIGHTNESS_PCT, ATTR_RGB_COLOR as ATTR_RGB_COLOR, ATTR_SUPPORTED_COLOR_MODES as ATTR_SUPPORTED_COLOR_MODES, DOMAIN as DOMAIN, brightness_supported as brightness_supported, color_supported as color_supported
from _typeshed import Incomplete
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, SERVICE_TURN_ON as SERVICE_TURN_ON
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import intent as intent

_LOGGER: Incomplete
INTENT_SET: str

async def async_setup_intents(hass: HomeAssistant) -> None: ...

class SetIntentHandler(intent.IntentHandler):
    intent_type = INTENT_SET
    slot_schema: Incomplete
    async def async_handle(self, intent_obj: intent.Intent) -> intent.IntentResponse: ...

from . import ATTR_BRIGHTNESS_PCT as ATTR_BRIGHTNESS_PCT, ATTR_RGB_COLOR as ATTR_RGB_COLOR, ATTR_SUPPORTED_COLOR_MODES as ATTR_SUPPORTED_COLOR_MODES, DOMAIN as DOMAIN, SERVICE_TURN_ON as SERVICE_TURN_ON, brightness_supported as brightness_supported, color_supported as color_supported
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID
from homeassistant.core import HomeAssistant as HomeAssistant, State as State
from homeassistant.helpers import intent as intent
from typing import Any

INTENT_SET: str

async def async_setup_intents(hass: HomeAssistant) -> None: ...
def _test_supports_color(state: State) -> None: ...
def _test_supports_brightness(state: State) -> None: ...

class SetIntentHandler(intent.IntentHandler):
    intent_type: Any
    slot_schema: Any
    async def async_handle(self, intent_obj: intent.Intent) -> intent.IntentResponse: ...

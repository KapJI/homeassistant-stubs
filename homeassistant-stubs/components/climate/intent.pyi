from . import ATTR_FAN_MODE as ATTR_FAN_MODE, ATTR_FAN_MODES as ATTR_FAN_MODES, ATTR_TEMPERATURE as ATTR_TEMPERATURE, ClimateEntityFeature as ClimateEntityFeature, INTENT_SET_FAN_MODE as INTENT_SET_FAN_MODE, INTENT_SET_TEMPERATURE as INTENT_SET_TEMPERATURE, SERVICE_SET_FAN_MODE as SERVICE_SET_FAN_MODE, SERVICE_SET_TEMPERATURE as SERVICE_SET_TEMPERATURE
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID
from homeassistant.core import HomeAssistant as HomeAssistant, State as State
from homeassistant.helpers import intent as intent, translation as translation
from typing import override

FAN_MODE_TRANSLATION_PREFIX: Incomplete

async def async_setup_intents(hass: HomeAssistant) -> None: ...

class SetTemperatureIntent(intent.IntentHandler):
    intent_type = INTENT_SET_TEMPERATURE
    description: str
    slot_schema: Incomplete
    platforms: Incomplete
    @override
    async def async_handle(self, intent_obj: intent.Intent) -> intent.IntentResponse: ...

class SetFanModeIntent(intent.IntentHandler):
    intent_type = INTENT_SET_FAN_MODE
    description: str
    slot_schema: Incomplete
    platforms: Incomplete
    @override
    async def async_handle(self, intent_obj: intent.Intent) -> intent.IntentResponse: ...

async def _async_resolve_fan_mode(hass: HomeAssistant, language: str, climate_state: State, requested: str) -> str | None: ...

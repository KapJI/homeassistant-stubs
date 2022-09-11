from .const import DATA_LIFX_MANAGER as DATA_LIFX_MANAGER, DOMAIN as DOMAIN, _LOGGER as _LOGGER
from .util import convert_8_to_16 as convert_8_to_16, find_hsbk as find_hsbk
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ATTR_BRIGHTNESS_PCT as ATTR_BRIGHTNESS_PCT, ATTR_COLOR_NAME as ATTR_COLOR_NAME, ATTR_COLOR_TEMP as ATTR_COLOR_TEMP, ATTR_HS_COLOR as ATTR_HS_COLOR, ATTR_KELVIN as ATTR_KELVIN, ATTR_RGB_COLOR as ATTR_RGB_COLOR, ATTR_TRANSITION as ATTR_TRANSITION, ATTR_XY_COLOR as ATTR_XY_COLOR, COLOR_GROUP as COLOR_GROUP, VALID_BRIGHTNESS as VALID_BRIGHTNESS, VALID_BRIGHTNESS_PCT as VALID_BRIGHTNESS_PCT, preprocess_turn_on_alternatives as preprocess_turn_on_alternatives
from homeassistant.const import ATTR_MODE as ATTR_MODE
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.helpers.service import async_extract_referenced_entity_ids as async_extract_referenced_entity_ids
from typing import Any

SCAN_INTERVAL: Incomplete
SERVICE_EFFECT_PULSE: str
SERVICE_EFFECT_COLORLOOP: str
SERVICE_EFFECT_STOP: str
ATTR_POWER_ON: str
ATTR_PERIOD: str
ATTR_CYCLES: str
ATTR_SPREAD: str
ATTR_CHANGE: str
PULSE_MODE_BLINK: str
PULSE_MODE_BREATHE: str
PULSE_MODE_PING: str
PULSE_MODE_STROBE: str
PULSE_MODE_SOLID: str
PULSE_MODES: Incomplete
LIFX_EFFECT_SCHEMA: Incomplete
LIFX_EFFECT_PULSE_SCHEMA: Incomplete
LIFX_EFFECT_COLORLOOP_SCHEMA: Incomplete
LIFX_EFFECT_STOP_SCHEMA: Incomplete
SERVICES: Incomplete

class LIFXManager:
    hass: Incomplete
    effects_conductor: Incomplete
    entry_id_to_entity_id: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    def async_unload(self) -> None: ...
    def async_register_entity(self, entity_id: str, entry_id: str) -> Callable[[], None]: ...
    def async_setup(self) -> None: ...
    async def start_effect(self, entity_ids: set[str], service: str, **kwargs: Any) -> None: ...

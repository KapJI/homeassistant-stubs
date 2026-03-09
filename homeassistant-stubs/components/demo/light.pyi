from . import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ATTR_COLOR_TEMP_KELVIN as ATTR_COLOR_TEMP_KELVIN, ATTR_EFFECT as ATTR_EFFECT, ATTR_HS_COLOR as ATTR_HS_COLOR, ATTR_RGBWW_COLOR as ATTR_RGBWW_COLOR, ATTR_RGBW_COLOR as ATTR_RGBW_COLOR, ATTR_WHITE as ATTR_WHITE, ColorMode as ColorMode, DEFAULT_MAX_KELVIN as DEFAULT_MAX_KELVIN, DEFAULT_MIN_KELVIN as DEFAULT_MIN_KELVIN, EFFECT_OFF as EFFECT_OFF, LightEntity as LightEntity, LightEntityFeature as LightEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any

LIGHT_COLORS: Incomplete
LIGHT_EFFECT_LIST: Incomplete
LIGHT_TEMPS: Incomplete
SUPPORT_DEMO: Incomplete
SUPPORT_DEMO_HS_WHITE: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class DemoLight(LightEntity):
    _attr_has_entity_name: bool
    _attr_name: Incomplete
    _attr_should_poll: bool
    _attr_max_color_temp_kelvin = DEFAULT_MAX_KELVIN
    _attr_min_color_temp_kelvin = DEFAULT_MIN_KELVIN
    _attr_translation_key: Incomplete
    _attr_brightness: Incomplete
    _attr_color_temp_kelvin: Incomplete
    _attr_effect: Incomplete
    _attr_effect_list: Incomplete
    _attr_hs_color: Incomplete
    _attr_rgbw_color: Incomplete
    _attr_rgbww_color: Incomplete
    _attr_is_on: Incomplete
    _attr_unique_id: Incomplete
    _attr_color_mode: Incomplete
    _attr_supported_color_modes: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, unique_id: str, device_name: str, state: bool, brightness: int = 180, ct: int | None = None, effect_list: list[str] | None = None, effect: str | None = None, hs_color: tuple[int, int] | None = None, rgbw_color: tuple[int, int, int, int] | None = None, rgbww_color: tuple[int, int, int, int, int] | None = None, supported_color_modes: set[ColorMode] | None = None, translation_key: str | None = None) -> None: ...
    @property
    def available(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...

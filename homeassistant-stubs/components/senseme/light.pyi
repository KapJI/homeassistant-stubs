from .const import DOMAIN as DOMAIN
from .entity import SensemeEntity as SensemeEntity
from aiosenseme import SensemeDevice as SensemeDevice
from homeassistant import config_entries as config_entries
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ATTR_COLOR_TEMP as ATTR_COLOR_TEMP, COLOR_MODE_BRIGHTNESS as COLOR_MODE_BRIGHTNESS, COLOR_MODE_COLOR_TEMP as COLOR_MODE_COLOR_TEMP, LightEntity as LightEntity
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.util.color import color_temperature_kelvin_to_mired as color_temperature_kelvin_to_mired, color_temperature_mired_to_kelvin as color_temperature_mired_to_kelvin
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: config_entries.ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class HASensemeLight(SensemeEntity, LightEntity):
    _attr_unique_id: Any
    def __init__(self, device: SensemeDevice, name: str) -> None: ...
    _attr_is_on: Any
    _attr_brightness: Any
    def _async_update_attrs(self) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...

class HASensemeFanLight(HASensemeLight):
    _attr_supported_color_modes: Any
    _attr_color_mode: Any
    def __init__(self, device: SensemeDevice) -> None: ...

class HASensemeStandaloneLight(HASensemeLight):
    _attr_supported_color_modes: Any
    _attr_color_mode: Any
    _attr_min_mireds: Any
    _attr_max_mireds: Any
    def __init__(self, device: SensemeDevice) -> None: ...
    _attr_color_temp: Any
    def _async_update_attrs(self) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...

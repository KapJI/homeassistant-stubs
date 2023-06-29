from .const import DOMAIN as DOMAIN
from .entity import BAFEntity as BAFEntity
from .models import BAFData as BAFData
from _typeshed import Incomplete
from aiobafi6 import Device as Device
from homeassistant import config_entries as config_entries
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ATTR_COLOR_TEMP as ATTR_COLOR_TEMP, ColorMode as ColorMode, LightEntity as LightEntity
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.util.color import color_temperature_kelvin_to_mired as color_temperature_kelvin_to_mired, color_temperature_mired_to_kelvin as color_temperature_mired_to_kelvin
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: config_entries.ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class BAFLight(BAFEntity, LightEntity):
    _attr_is_on: Incomplete
    _attr_brightness: Incomplete
    def _async_update_attrs(self) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...

class BAFFanLight(BAFLight):
    _attr_name: Incomplete
    _attr_supported_color_modes: Incomplete
    _attr_color_mode: Incomplete
    def __init__(self, device: Device) -> None: ...

class BAFStandaloneLight(BAFLight):
    _attr_supported_color_modes: Incomplete
    _attr_color_mode: Incomplete
    _attr_min_mireds: Incomplete
    _attr_max_mireds: Incomplete
    def __init__(self, device: Device) -> None: ...
    _attr_color_temp: Incomplete
    def _async_update_attrs(self) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...

from .const import DiscoveryInfo as DiscoveryInfo, MYSENSORS_DISCOVERY as MYSENSORS_DISCOVERY, SensorType as SensorType
from .device import MySensorsDevice as MySensorsDevice
from .helpers import on_unload as on_unload
from homeassistant.components import mysensors as mysensors
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ATTR_RGBW_COLOR as ATTR_RGBW_COLOR, ATTR_RGB_COLOR as ATTR_RGB_COLOR, COLOR_MODE_BRIGHTNESS as COLOR_MODE_BRIGHTNESS, COLOR_MODE_RGB as COLOR_MODE_RGB, COLOR_MODE_RGBW as COLOR_MODE_RGBW, DOMAIN as DOMAIN, LightEntity as LightEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import STATE_OFF as STATE_OFF, STATE_ON as STATE_ON
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.util.color import rgb_hex_to_rgb_list as rgb_hex_to_rgb_list
from typing import Any

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class MySensorsLight(mysensors.device.MySensorsEntity, LightEntity):
    _state: Any
    def __init__(self, *args: Any) -> None: ...
    @property
    def is_on(self) -> bool: ...
    def _turn_on_light(self) -> None: ...
    _attr_brightness: Any
    def _turn_on_dimmer(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    def _async_update_light(self) -> None: ...
    def _async_update_dimmer(self) -> None: ...

class MySensorsLightDimmer(MySensorsLight):
    _attr_supported_color_modes: Any
    _attr_color_mode: Any
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_update(self) -> None: ...

class MySensorsLightRGB(MySensorsLight):
    _attr_supported_color_modes: Any
    _attr_color_mode: Any
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    _attr_rgb_color: Any
    def _turn_on_rgb(self, **kwargs: Any) -> None: ...
    async def async_update(self) -> None: ...
    def _async_update_rgb_or_w(self) -> None: ...

class MySensorsLightRGBW(MySensorsLightRGB):
    _attr_supported_color_modes: Any
    _attr_color_mode: Any
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    _attr_rgbw_color: Any
    def _turn_on_rgbw(self, **kwargs: Any) -> None: ...
    def _async_update_rgb_or_w(self) -> None: ...

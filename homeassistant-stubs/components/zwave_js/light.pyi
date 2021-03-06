from .const import DATA_CLIENT as DATA_CLIENT, DOMAIN as DOMAIN
from .discovery import ZwaveDiscoveryInfo as ZwaveDiscoveryInfo
from .entity import ZWaveBaseEntity as ZWaveBaseEntity
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ATTR_COLOR_TEMP as ATTR_COLOR_TEMP, ATTR_HS_COLOR as ATTR_HS_COLOR, ATTR_RGBW_COLOR as ATTR_RGBW_COLOR, ATTR_TRANSITION as ATTR_TRANSITION, COLOR_MODE_BRIGHTNESS as COLOR_MODE_BRIGHTNESS, COLOR_MODE_COLOR_TEMP as COLOR_MODE_COLOR_TEMP, COLOR_MODE_HS as COLOR_MODE_HS, COLOR_MODE_RGBW as COLOR_MODE_RGBW, LightEntity as LightEntity, SUPPORT_TRANSITION as SUPPORT_TRANSITION
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any
from zwave_js_server.client import Client as ZwaveClient
from zwave_js_server.const.command_class.color_switch import ColorComponent

LOGGER: Any
MULTI_COLOR_MAP: Any
TRANSITION_DURATION: str

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
def byte_to_zwave_brightness(value: int) -> int: ...

class ZwaveLight(ZWaveBaseEntity, LightEntity):
    _supports_color: bool
    _supports_rgbw: bool
    _supports_color_temp: bool
    _hs_color: Any
    _rgbw_color: Any
    _color_mode: Any
    _color_temp: Any
    _min_mireds: int
    _max_mireds: int
    _warm_white: Any
    _cold_white: Any
    _supported_color_modes: Any
    _target_brightness: Any
    _target_color: Any
    _attr_supported_features: int
    supports_brightness_transition: Any
    supports_color_transition: Any
    def __init__(self, config_entry: ConfigEntry, client: ZwaveClient, info: ZwaveDiscoveryInfo) -> None: ...
    def on_value_update(self) -> None: ...
    @property
    def brightness(self) -> int: ...
    @property
    def color_mode(self) -> Union[str, None]: ...
    @property
    def is_on(self) -> bool: ...
    @property
    def hs_color(self) -> Union[tuple[float, float], None]: ...
    @property
    def rgbw_color(self) -> Union[tuple[int, int, int, int], None]: ...
    @property
    def color_temp(self) -> Union[int, None]: ...
    @property
    def min_mireds(self) -> int: ...
    @property
    def max_mireds(self) -> int: ...
    @property
    def supported_color_modes(self) -> Union[set, None]: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def _async_set_colors(self, colors: dict[ColorComponent, int], transition: Union[float, None] = ...) -> None: ...
    async def _async_set_brightness(self, brightness: Union[int, None], transition: Union[float, None] = ...) -> None: ...
    def _calculate_color_values(self) -> None: ...

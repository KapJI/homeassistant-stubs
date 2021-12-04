from . import FluxLedUpdateCoordinator as FluxLedUpdateCoordinator
from .const import CONF_AUTOMATIC_ADD as CONF_AUTOMATIC_ADD, CONF_COLORS as CONF_COLORS, CONF_CUSTOM_EFFECT as CONF_CUSTOM_EFFECT, CONF_CUSTOM_EFFECT_COLORS as CONF_CUSTOM_EFFECT_COLORS, CONF_CUSTOM_EFFECT_SPEED_PCT as CONF_CUSTOM_EFFECT_SPEED_PCT, CONF_CUSTOM_EFFECT_TRANSITION as CONF_CUSTOM_EFFECT_TRANSITION, CONF_SPEED_PCT as CONF_SPEED_PCT, CONF_TRANSITION as CONF_TRANSITION, DEFAULT_EFFECT_SPEED as DEFAULT_EFFECT_SPEED, DOMAIN as DOMAIN, FLUX_LED_DISCOVERY as FLUX_LED_DISCOVERY, MODE_AUTO as MODE_AUTO, MODE_RGB as MODE_RGB, MODE_RGBW as MODE_RGBW, MODE_WHITE as MODE_WHITE, TRANSITION_GRADUAL as TRANSITION_GRADUAL, TRANSITION_JUMP as TRANSITION_JUMP, TRANSITION_STROBE as TRANSITION_STROBE
from .entity import FluxOnOffEntity as FluxOnOffEntity
from .util import _effect_brightness as _effect_brightness, _flux_color_mode_to_hass as _flux_color_mode_to_hass, _hass_color_modes as _hass_color_modes
from homeassistant import config_entries as config_entries
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ATTR_COLOR_TEMP as ATTR_COLOR_TEMP, ATTR_EFFECT as ATTR_EFFECT, ATTR_RGBWW_COLOR as ATTR_RGBWW_COLOR, ATTR_RGBW_COLOR as ATTR_RGBW_COLOR, ATTR_RGB_COLOR as ATTR_RGB_COLOR, ATTR_WHITE as ATTR_WHITE, COLOR_MODE_RGBWW as COLOR_MODE_RGBWW, LightEntity as LightEntity, PLATFORM_SCHEMA as PLATFORM_SCHEMA, SUPPORT_EFFECT as SUPPORT_EFFECT, SUPPORT_TRANSITION as SUPPORT_TRANSITION
from homeassistant.const import ATTR_MODE as ATTR_MODE, CONF_DEVICES as CONF_DEVICES, CONF_HOST as CONF_HOST, CONF_MAC as CONF_MAC, CONF_MODE as CONF_MODE, CONF_NAME as CONF_NAME, CONF_PROTOCOL as CONF_PROTOCOL
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import entity_platform as entity_platform
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from homeassistant.util.color import color_temperature_kelvin_to_mired as color_temperature_kelvin_to_mired, color_temperature_mired_to_kelvin as color_temperature_mired_to_kelvin
from typing import Any, Final

_LOGGER: Any
MODE_ATTRS: Any
COLOR_TEMP_WARM_VS_COLD_WHITE_CUT_OFF: Final[int]
EFFECT_CUSTOM: Final[str]
SERVICE_CUSTOM_EFFECT: Final[str]
CUSTOM_EFFECT_DICT: Final[Any]
CUSTOM_EFFECT_SCHEMA: Final[Any]
DEVICE_SCHEMA: Final[Any]

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: Union[DiscoveryInfoType, None] = ...) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: config_entries.ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class FluxLight(FluxOnOffEntity, CoordinatorEntity, LightEntity):
    _attr_supported_features: Any
    _attr_min_mireds: Any
    _attr_max_mireds: Any
    _attr_supported_color_modes: Any
    _attr_effect_list: Any
    _custom_effect_colors: Any
    _custom_effect_speed_pct: Any
    _custom_effect_transition: Any
    def __init__(self, coordinator: FluxLedUpdateCoordinator, unique_id: Union[str, None], name: str, custom_effect_colors: list[tuple[int, int, int]], custom_effect_speed_pct: int, custom_effect_transition: str) -> None: ...
    @property
    def brightness(self) -> int: ...
    @property
    def color_temp(self) -> int: ...
    @property
    def rgb_color(self) -> tuple[int, int, int]: ...
    @property
    def rgbw_color(self) -> tuple[int, int, int, int]: ...
    @property
    def rgbww_color(self) -> tuple[int, int, int, int, int]: ...
    @property
    def color_mode(self) -> str: ...
    @property
    def effect(self) -> Union[str, None]: ...
    async def _async_turn_on(self, **kwargs: Any) -> None: ...
    async def _async_set_effect(self, effect: str, brightness: int) -> None: ...
    def _async_brightness(self, **kwargs: Any) -> int: ...
    async def _async_set_mode(self, **kwargs: Any) -> None: ...
    async def async_set_custom_effect(self, colors: list[tuple[int, int, int]], speed_pct: int, transition: str) -> None: ...

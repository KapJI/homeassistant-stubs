from . import FluxLedUpdateCoordinator as FluxLedUpdateCoordinator
from .const import CONF_AUTOMATIC_ADD as CONF_AUTOMATIC_ADD, CONF_COLORS as CONF_COLORS, CONF_CUSTOM_EFFECT as CONF_CUSTOM_EFFECT, CONF_CUSTOM_EFFECT_COLORS as CONF_CUSTOM_EFFECT_COLORS, CONF_CUSTOM_EFFECT_SPEED_PCT as CONF_CUSTOM_EFFECT_SPEED_PCT, CONF_CUSTOM_EFFECT_TRANSITION as CONF_CUSTOM_EFFECT_TRANSITION, CONF_SPEED_PCT as CONF_SPEED_PCT, CONF_TRANSITION as CONF_TRANSITION, DEFAULT_EFFECT_SPEED as DEFAULT_EFFECT_SPEED, DOMAIN as DOMAIN, FLUX_HOST as FLUX_HOST, FLUX_LED_DISCOVERY as FLUX_LED_DISCOVERY, FLUX_MAC as FLUX_MAC, MODE_AUTO as MODE_AUTO, MODE_RGB as MODE_RGB, MODE_RGBW as MODE_RGBW, MODE_WHITE as MODE_WHITE, TRANSITION_GRADUAL as TRANSITION_GRADUAL, TRANSITION_JUMP as TRANSITION_JUMP, TRANSITION_STROBE as TRANSITION_STROBE
from .entity import FluxEntity as FluxEntity
from homeassistant import config_entries as config_entries
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ATTR_COLOR_TEMP as ATTR_COLOR_TEMP, ATTR_EFFECT as ATTR_EFFECT, ATTR_RGBWW_COLOR as ATTR_RGBWW_COLOR, ATTR_RGBW_COLOR as ATTR_RGBW_COLOR, ATTR_RGB_COLOR as ATTR_RGB_COLOR, ATTR_WHITE as ATTR_WHITE, COLOR_MODE_BRIGHTNESS as COLOR_MODE_BRIGHTNESS, COLOR_MODE_COLOR_TEMP as COLOR_MODE_COLOR_TEMP, COLOR_MODE_ONOFF as COLOR_MODE_ONOFF, COLOR_MODE_RGB as COLOR_MODE_RGB, COLOR_MODE_RGBW as COLOR_MODE_RGBW, COLOR_MODE_RGBWW as COLOR_MODE_RGBWW, COLOR_MODE_WHITE as COLOR_MODE_WHITE, EFFECT_COLORLOOP as EFFECT_COLORLOOP, EFFECT_RANDOM as EFFECT_RANDOM, LightEntity as LightEntity, PLATFORM_SCHEMA as PLATFORM_SCHEMA, SUPPORT_EFFECT as SUPPORT_EFFECT, SUPPORT_TRANSITION as SUPPORT_TRANSITION
from homeassistant.const import ATTR_MODE as ATTR_MODE, CONF_DEVICES as CONF_DEVICES, CONF_HOST as CONF_HOST, CONF_MAC as CONF_MAC, CONF_MODE as CONF_MODE, CONF_NAME as CONF_NAME, CONF_PROTOCOL as CONF_PROTOCOL
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import entity_platform as entity_platform
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from homeassistant.util.color import color_RGB_to_hs as color_RGB_to_hs, color_hs_to_RGB as color_hs_to_RGB, color_temperature_kelvin_to_mired as color_temperature_kelvin_to_mired, color_temperature_mired_to_kelvin as color_temperature_mired_to_kelvin
from typing import Any, Final

_LOGGER: Any
SUPPORT_FLUX_LED: Final[Any]
FLUX_COLOR_MODE_TO_HASS: Final[Any]
EFFECT_SUPPORT_MODES: Any
COLOR_TEMP_WARM_VS_COLD_WHITE_CUT_OFF: Final[int]
EFFECT_RED_FADE: Final[str]
EFFECT_GREEN_FADE: Final[str]
EFFECT_BLUE_FADE: Final[str]
EFFECT_YELLOW_FADE: Final[str]
EFFECT_CYAN_FADE: Final[str]
EFFECT_PURPLE_FADE: Final[str]
EFFECT_WHITE_FADE: Final[str]
EFFECT_RED_GREEN_CROSS_FADE: Final[str]
EFFECT_RED_BLUE_CROSS_FADE: Final[str]
EFFECT_GREEN_BLUE_CROSS_FADE: Final[str]
EFFECT_COLORSTROBE: Final[str]
EFFECT_RED_STROBE: Final[str]
EFFECT_GREEN_STROBE: Final[str]
EFFECT_BLUE_STROBE: Final[str]
EFFECT_YELLOW_STROBE: Final[str]
EFFECT_CYAN_STROBE: Final[str]
EFFECT_PURPLE_STROBE: Final[str]
EFFECT_WHITE_STROBE: Final[str]
EFFECT_COLORJUMP: Final[str]
EFFECT_CUSTOM: Final[str]
EFFECT_MAP: Final[Any]
EFFECT_ID_NAME: Final[Any]
EFFECT_CUSTOM_CODE: Final[int]
FLUX_EFFECT_LIST: Final[Any]
SERVICE_CUSTOM_EFFECT: Final[str]
CUSTOM_EFFECT_DICT: Final[Any]
CUSTOM_EFFECT_SCHEMA: Final[Any]
DEVICE_SCHEMA: Final[Any]

def _flux_color_mode_to_hass(flux_color_mode: str, flux_color_modes: set[str]) -> str: ...
async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: Union[DiscoveryInfoType, None] = ...) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: config_entries.ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class FluxLight(FluxEntity, CoordinatorEntity, LightEntity):
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
    def rgbwc_color(self) -> tuple[int, int, int, int, int]: ...
    @property
    def color_mode(self) -> str: ...
    @property
    def effect(self) -> Union[str, None]: ...
    async def _async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_set_custom_effect(self, colors: list[tuple[int, int, int]], speed_pct: int, transition: str) -> None: ...

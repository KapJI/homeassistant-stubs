from collections.abc import Iterable
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import SERVICE_TOGGLE as SERVICE_TOGGLE, SERVICE_TURN_OFF as SERVICE_TURN_OFF, SERVICE_TURN_ON as SERVICE_TURN_ON, STATE_ON as STATE_ON
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.config_validation import PLATFORM_SCHEMA as PLATFORM_SCHEMA, PLATFORM_SCHEMA_BASE as PLATFORM_SCHEMA_BASE, make_entity_service_schema as make_entity_service_schema
from homeassistant.helpers.entity import ToggleEntity as ToggleEntity, ToggleEntityDescription as ToggleEntityDescription
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.loader import bind_hass as bind_hass
from typing import Any

DOMAIN: str
SCAN_INTERVAL: Any
DATA_PROFILES: str
ENTITY_ID_FORMAT: Any
SUPPORT_BRIGHTNESS: int
SUPPORT_COLOR_TEMP: int
SUPPORT_EFFECT: int
SUPPORT_FLASH: int
SUPPORT_COLOR: int
SUPPORT_TRANSITION: int
SUPPORT_WHITE_VALUE: int
ATTR_COLOR_MODE: str
ATTR_SUPPORTED_COLOR_MODES: str
COLOR_MODE_UNKNOWN: str
COLOR_MODE_ONOFF: str
COLOR_MODE_BRIGHTNESS: str
COLOR_MODE_COLOR_TEMP: str
COLOR_MODE_HS: str
COLOR_MODE_XY: str
COLOR_MODE_RGB: str
COLOR_MODE_RGBW: str
COLOR_MODE_RGBWW: str
COLOR_MODE_WHITE: str
VALID_COLOR_MODES: Any
COLOR_MODES_BRIGHTNESS: Any
COLOR_MODES_COLOR: Any

def valid_supported_color_modes(color_modes: Iterable[str]) -> set[str]: ...
def brightness_supported(color_modes: Union[Iterable[str], None]) -> bool: ...
def color_supported(color_modes: Union[Iterable[str], None]) -> bool: ...
def color_temp_supported(color_modes: Union[Iterable[str], None]) -> bool: ...
def get_supported_color_modes(hass: HomeAssistant, entity_id: str) -> Union[set, None]: ...

ATTR_TRANSITION: str
ATTR_RGB_COLOR: str
ATTR_RGBW_COLOR: str
ATTR_RGBWW_COLOR: str
ATTR_XY_COLOR: str
ATTR_HS_COLOR: str
ATTR_COLOR_TEMP: str
ATTR_KELVIN: str
ATTR_MIN_MIREDS: str
ATTR_MAX_MIREDS: str
ATTR_COLOR_NAME: str
ATTR_WHITE_VALUE: str
ATTR_WHITE: str
ATTR_BRIGHTNESS: str
ATTR_BRIGHTNESS_PCT: str
ATTR_BRIGHTNESS_STEP: str
ATTR_BRIGHTNESS_STEP_PCT: str
ATTR_PROFILE: str
ATTR_FLASH: str
FLASH_SHORT: str
FLASH_LONG: str
ATTR_EFFECT_LIST: str
ATTR_EFFECT: str
EFFECT_COLORLOOP: str
EFFECT_RANDOM: str
EFFECT_WHITE: str
COLOR_GROUP: str
LIGHT_PROFILES_FILE: str
VALID_TRANSITION: Any
VALID_BRIGHTNESS: Any
VALID_BRIGHTNESS_PCT: Any
VALID_BRIGHTNESS_STEP: Any
VALID_BRIGHTNESS_STEP_PCT: Any
VALID_FLASH: Any
LIGHT_TURN_ON_SCHEMA: Any
LIGHT_TURN_OFF_SCHEMA: Any
_LOGGER: Any

def is_on(hass: HomeAssistant, entity_id: str) -> bool: ...
def preprocess_turn_on_alternatives(hass, params) -> None: ...
def filter_turn_off_params(light, params): ...
def filter_turn_on_params(light, params): ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
def _coerce_none(value: str) -> None: ...

class Profile:
    name: str
    color_x: Union[float, None]
    color_y: Union[float, None]
    brightness: Union[int, None]
    transition: Union[int, None]
    hs_color: Union[tuple[float, float], None]
    SCHEMA: Any
    def __post_init__(self) -> None: ...
    @classmethod
    def from_csv_row(cls, csv_row: list[str]) -> Profile: ...
    def __init__(self, name, color_x, color_y, brightness, transition) -> None: ...

class Profiles:
    hass: Any
    data: Any
    def __init__(self, hass: HomeAssistant) -> None: ...
    def _load_profile_data(self) -> dict[str, Profile]: ...
    async def async_initialize(self) -> None: ...
    def apply_default(self, entity_id: str, state_on: bool, params: dict) -> None: ...
    def apply_profile(self, name: str, params: dict) -> None: ...

class LightEntityDescription(ToggleEntityDescription):
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, force_update, icon, name, unit_of_measurement) -> None: ...

class LightEntity(ToggleEntity):
    entity_description: LightEntityDescription
    _attr_brightness: Union[int, None]
    _attr_color_mode: Union[str, None]
    _attr_color_temp: Union[int, None]
    _attr_effect_list: Union[list[str], None]
    _attr_effect: Union[str, None]
    _attr_hs_color: Union[tuple[float, float], None]
    _attr_max_mireds: int
    _attr_min_mireds: int
    _attr_rgb_color: Union[tuple[int, int, int], None]
    _attr_rgbw_color: Union[tuple[int, int, int, int], None]
    _attr_rgbww_color: Union[tuple[int, int, int, int, int], None]
    _attr_supported_color_modes: Union[set[str], None]
    _attr_supported_features: int
    _attr_xy_color: Union[tuple[float, float], None]
    @property
    def brightness(self) -> Union[int, None]: ...
    @property
    def color_mode(self) -> Union[str, None]: ...
    @property
    def _light_internal_color_mode(self) -> str: ...
    @property
    def hs_color(self) -> Union[tuple[float, float], None]: ...
    @property
    def xy_color(self) -> Union[tuple[float, float], None]: ...
    @property
    def rgb_color(self) -> Union[tuple[int, int, int], None]: ...
    @property
    def rgbw_color(self) -> Union[tuple[int, int, int, int], None]: ...
    @property
    def _light_internal_rgbw_color(self) -> Union[tuple[int, int, int, int], None]: ...
    @property
    def rgbww_color(self) -> Union[tuple[int, int, int, int, int], None]: ...
    @property
    def color_temp(self) -> Union[int, None]: ...
    @property
    def min_mireds(self) -> int: ...
    @property
    def max_mireds(self) -> int: ...
    @property
    def white_value(self) -> Union[int, None]: ...
    @property
    def effect_list(self) -> Union[list[str], None]: ...
    @property
    def effect(self) -> Union[str, None]: ...
    @property
    def capability_attributes(self): ...
    def _light_internal_convert_color(self, color_mode: str) -> dict: ...
    @property
    def state_attributes(self): ...
    @property
    def _light_internal_supported_color_modes(self) -> set: ...
    @property
    def supported_color_modes(self) -> Union[set[str], None]: ...
    @property
    def supported_features(self) -> int: ...

def legacy_supported_features(supported_features: int, supported_color_modes: Union[list[str], None]) -> int: ...

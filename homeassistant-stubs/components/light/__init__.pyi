from _typeshed import Incomplete
from collections.abc import Iterable
from enum import IntFlag, StrEnum
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import SERVICE_TOGGLE as SERVICE_TOGGLE, SERVICE_TURN_OFF as SERVICE_TURN_OFF, SERVICE_TURN_ON as SERVICE_TURN_ON, STATE_ON as STATE_ON
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.config_validation import PLATFORM_SCHEMA as PLATFORM_SCHEMA, PLATFORM_SCHEMA_BASE as PLATFORM_SCHEMA_BASE, make_entity_service_schema as make_entity_service_schema
from homeassistant.helpers.entity import ToggleEntity as ToggleEntity, ToggleEntityDescription as ToggleEntityDescription
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.loader import bind_hass as bind_hass
from typing import Any, Self

DOMAIN: str
SCAN_INTERVAL: Incomplete
DATA_PROFILES: str
ENTITY_ID_FORMAT: Incomplete

class LightEntityFeature(IntFlag):
    EFFECT: int
    FLASH: int
    TRANSITION: int

SUPPORT_BRIGHTNESS: int
SUPPORT_COLOR_TEMP: int
SUPPORT_EFFECT: int
SUPPORT_FLASH: int
SUPPORT_COLOR: int
SUPPORT_TRANSITION: int
ATTR_COLOR_MODE: str
ATTR_SUPPORTED_COLOR_MODES: str

class ColorMode(StrEnum):
    UNKNOWN: str
    ONOFF: str
    BRIGHTNESS: str
    COLOR_TEMP: str
    HS: str
    XY: str
    RGB: str
    RGBW: str
    RGBWW: str
    WHITE: str

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
VALID_COLOR_MODES: Incomplete
COLOR_MODES_BRIGHTNESS: Incomplete
COLOR_MODES_COLOR: Incomplete

def filter_supported_color_modes(color_modes: Iterable[ColorMode]) -> set[ColorMode]: ...
def valid_supported_color_modes(color_modes: Iterable[ColorMode | str]) -> set[ColorMode | str]: ...
def brightness_supported(color_modes: Iterable[ColorMode | str] | None) -> bool: ...
def color_supported(color_modes: Iterable[ColorMode | str] | None) -> bool: ...
def color_temp_supported(color_modes: Iterable[ColorMode | str] | None) -> bool: ...
def get_supported_color_modes(hass: HomeAssistant, entity_id: str) -> set[str] | None: ...

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
ATTR_COLOR_TEMP_KELVIN: str
ATTR_MIN_COLOR_TEMP_KELVIN: str
ATTR_MAX_COLOR_TEMP_KELVIN: str
ATTR_COLOR_NAME: str
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
VALID_TRANSITION: Incomplete
VALID_BRIGHTNESS: Incomplete
VALID_BRIGHTNESS_PCT: Incomplete
VALID_BRIGHTNESS_STEP: Incomplete
VALID_BRIGHTNESS_STEP_PCT: Incomplete
VALID_FLASH: Incomplete
LIGHT_TURN_ON_SCHEMA: Incomplete
LIGHT_TURN_OFF_SCHEMA: Incomplete
_LOGGER: Incomplete

def is_on(hass: HomeAssistant, entity_id: str) -> bool: ...
def preprocess_turn_on_alternatives(hass: HomeAssistant, params: dict[str, Any]) -> None: ...
def filter_turn_off_params(light: LightEntity, params: dict[str, Any]) -> dict[str, Any]: ...
def filter_turn_on_params(light: LightEntity, params: dict[str, Any]) -> dict[str, Any]: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
def _coerce_none(value: str) -> None: ...

class Profile:
    name: str
    color_x: float | None
    color_y: float | None
    brightness: int | None
    transition: int | None
    hs_color: tuple[float, float] | None
    SCHEMA: Incomplete
    def __post_init__(self) -> None: ...
    @classmethod
    def from_csv_row(cls, csv_row: list[str]) -> Self: ...
    def __init__(self, name, color_x, color_y, brightness, transition) -> None: ...

class Profiles:
    hass: Incomplete
    data: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    def _load_profile_data(self) -> dict[str, Profile]: ...
    async def async_initialize(self) -> None: ...
    def apply_default(self, entity_id: str, state_on: bool | None, params: dict[str, Any]) -> None: ...
    def apply_profile(self, name: str, params: dict[str, Any]) -> None: ...

class LightEntityDescription(ToggleEntityDescription):
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement) -> None: ...

class LightEntity(ToggleEntity):
    _entity_component_unrecorded_attributes: Incomplete
    entity_description: LightEntityDescription
    _attr_brightness: int | None
    _attr_color_mode: ColorMode | str | None
    _attr_color_temp: int | None
    _attr_color_temp_kelvin: int | None
    _attr_effect_list: list[str] | None
    _attr_effect: str | None
    _attr_hs_color: tuple[float, float] | None
    _attr_max_color_temp_kelvin: int | None
    _attr_min_color_temp_kelvin: int | None
    _attr_max_mireds: int
    _attr_min_mireds: int
    _attr_rgb_color: tuple[int, int, int] | None
    _attr_rgbw_color: tuple[int, int, int, int] | None
    _attr_rgbww_color: tuple[int, int, int, int, int] | None
    _attr_supported_color_modes: set[ColorMode] | set[str] | None
    _attr_supported_features: LightEntityFeature
    _attr_xy_color: tuple[float, float] | None
    @property
    def brightness(self) -> int | None: ...
    @property
    def color_mode(self) -> ColorMode | str | None: ...
    @property
    def _light_internal_color_mode(self) -> str: ...
    @property
    def hs_color(self) -> tuple[float, float] | None: ...
    @property
    def xy_color(self) -> tuple[float, float] | None: ...
    @property
    def rgb_color(self) -> tuple[int, int, int] | None: ...
    @property
    def rgbw_color(self) -> tuple[int, int, int, int] | None: ...
    @property
    def _light_internal_rgbw_color(self) -> tuple[int, int, int, int] | None: ...
    @property
    def rgbww_color(self) -> tuple[int, int, int, int, int] | None: ...
    @property
    def color_temp(self) -> int | None: ...
    @property
    def color_temp_kelvin(self) -> int | None: ...
    @property
    def min_mireds(self) -> int: ...
    @property
    def max_mireds(self) -> int: ...
    @property
    def min_color_temp_kelvin(self) -> int: ...
    @property
    def max_color_temp_kelvin(self) -> int: ...
    @property
    def effect_list(self) -> list[str] | None: ...
    @property
    def effect(self) -> str | None: ...
    @property
    def capability_attributes(self) -> dict[str, Any]: ...
    def _light_internal_convert_color(self, color_mode: ColorMode | str) -> dict[str, tuple[float, ...]]: ...
    @property
    def state_attributes(self) -> dict[str, Any] | None: ...
    @property
    def _light_internal_supported_color_modes(self) -> set[ColorMode] | set[str]: ...
    @property
    def supported_color_modes(self) -> set[ColorMode] | set[str] | None: ...
    @property
    def supported_features(self) -> LightEntityFeature: ...

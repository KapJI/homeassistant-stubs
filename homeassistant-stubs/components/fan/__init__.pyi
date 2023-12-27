from _typeshed import Incomplete
from dataclasses import dataclass
from enum import IntFlag
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import SERVICE_TOGGLE as SERVICE_TOGGLE, SERVICE_TURN_OFF as SERVICE_TURN_OFF, SERVICE_TURN_ON as SERVICE_TURN_ON, STATE_ON as STATE_ON
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ServiceValidationError as ServiceValidationError
from homeassistant.helpers.config_validation import PLATFORM_SCHEMA as PLATFORM_SCHEMA, PLATFORM_SCHEMA_BASE as PLATFORM_SCHEMA_BASE
from homeassistant.helpers.entity import ToggleEntity as ToggleEntity, ToggleEntityDescription as ToggleEntityDescription
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.loader import bind_hass as bind_hass
from homeassistant.util.percentage import percentage_to_ranged_value as percentage_to_ranged_value, ranged_value_to_percentage as ranged_value_to_percentage
from typing import Any

_LOGGER: Incomplete
DOMAIN: str
SCAN_INTERVAL: Incomplete
ENTITY_ID_FORMAT: Incomplete

class FanEntityFeature(IntFlag):
    SET_SPEED: int
    OSCILLATE: int
    DIRECTION: int
    PRESET_MODE: int

SUPPORT_SET_SPEED: int
SUPPORT_OSCILLATE: int
SUPPORT_DIRECTION: int
SUPPORT_PRESET_MODE: int
SERVICE_INCREASE_SPEED: str
SERVICE_DECREASE_SPEED: str
SERVICE_OSCILLATE: str
SERVICE_SET_DIRECTION: str
SERVICE_SET_PERCENTAGE: str
SERVICE_SET_PRESET_MODE: str
DIRECTION_FORWARD: str
DIRECTION_REVERSE: str
ATTR_PERCENTAGE: str
ATTR_PERCENTAGE_STEP: str
ATTR_OSCILLATING: str
ATTR_DIRECTION: str
ATTR_PRESET_MODE: str
ATTR_PRESET_MODES: str

class NotValidPresetModeError(ServiceValidationError):
    def __init__(self, *args: object, translation_placeholders: dict[str, str] | None = None) -> None: ...

def is_on(hass: HomeAssistant, entity_id: str) -> bool: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

@dataclass
class FanEntityDescription(ToggleEntityDescription):
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement) -> None: ...

class FanEntity(ToggleEntity):
    _entity_component_unrecorded_attributes: Incomplete
    entity_description: FanEntityDescription
    _attr_current_direction: str | None
    _attr_oscillating: bool | None
    _attr_percentage: int | None
    _attr_preset_mode: str | None
    _attr_preset_modes: list[str] | None
    _attr_speed_count: int
    _attr_supported_features: FanEntityFeature
    def set_percentage(self, percentage: int) -> None: ...
    async def async_set_percentage(self, percentage: int) -> None: ...
    async def async_increase_speed(self, percentage_step: int | None = None) -> None: ...
    async def async_decrease_speed(self, percentage_step: int | None = None) -> None: ...
    async def _async_adjust_speed(self, modifier: int, percentage_step: int | None) -> None: ...
    def set_preset_mode(self, preset_mode: str) -> None: ...
    async def async_handle_set_preset_mode_service(self, preset_mode: str) -> None: ...
    async def async_set_preset_mode(self, preset_mode: str) -> None: ...
    def _valid_preset_mode_or_raise(self, preset_mode: str) -> None: ...
    def set_direction(self, direction: str) -> None: ...
    async def async_set_direction(self, direction: str) -> None: ...
    def turn_on(self, percentage: int | None = None, preset_mode: str | None = None, **kwargs: Any) -> None: ...
    async def async_handle_turn_on_service(self, percentage: int | None = None, preset_mode: str | None = None, **kwargs: Any) -> None: ...
    async def async_turn_on(self, percentage: int | None = None, preset_mode: str | None = None, **kwargs: Any) -> None: ...
    def oscillate(self, oscillating: bool) -> None: ...
    async def async_oscillate(self, oscillating: bool) -> None: ...
    @property
    def is_on(self) -> bool | None: ...
    @property
    def percentage(self) -> int | None: ...
    @property
    def speed_count(self) -> int: ...
    @property
    def percentage_step(self) -> float: ...
    @property
    def current_direction(self) -> str | None: ...
    @property
    def oscillating(self) -> bool | None: ...
    @property
    def capability_attributes(self) -> dict[str, list[str] | None]: ...
    @property
    def state_attributes(self) -> dict[str, float | str | None]: ...
    @property
    def supported_features(self) -> FanEntityFeature: ...
    @property
    def preset_mode(self) -> str | None: ...
    @property
    def preset_modes(self) -> list[str] | None: ...

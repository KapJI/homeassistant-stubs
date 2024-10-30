from .const import DOMAIN as DOMAIN, STATE_CLEANING as STATE_CLEANING, STATE_DOCKED as STATE_DOCKED, STATE_ERROR as STATE_ERROR, STATE_RETURNING as STATE_RETURNING
from _typeshed import Incomplete
from enum import IntFlag
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_BATTERY_LEVEL as ATTR_BATTERY_LEVEL, ATTR_COMMAND as ATTR_COMMAND, SERVICE_TOGGLE as SERVICE_TOGGLE, SERVICE_TURN_OFF as SERVICE_TURN_OFF, SERVICE_TURN_ON as SERVICE_TURN_ON, STATE_IDLE as STATE_IDLE, STATE_ON as STATE_ON, STATE_PAUSED as STATE_PAUSED
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.deprecation import DeprecatedConstantEnum as DeprecatedConstantEnum, all_with_deprecated_constants as all_with_deprecated_constants, check_if_deprecated_constant as check_if_deprecated_constant, dir_with_deprecated_constants as dir_with_deprecated_constants
from homeassistant.helpers.entity import Entity as Entity, EntityDescription as EntityDescription
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.icon import icon_for_battery_level as icon_for_battery_level
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.loader import bind_hass as bind_hass
from homeassistant.util.hass_dict import HassKey as HassKey
from typing import Any

_LOGGER: Incomplete
DATA_COMPONENT: HassKey[EntityComponent[StateVacuumEntity]]
ENTITY_ID_FORMAT: Incomplete
PLATFORM_SCHEMA: Incomplete
PLATFORM_SCHEMA_BASE: Incomplete
SCAN_INTERVAL: Incomplete
ATTR_BATTERY_ICON: str
ATTR_CLEANED_AREA: str
ATTR_FAN_SPEED: str
ATTR_FAN_SPEED_LIST: str
ATTR_PARAMS: str
ATTR_STATUS: str
SERVICE_CLEAN_SPOT: str
SERVICE_LOCATE: str
SERVICE_RETURN_TO_BASE: str
SERVICE_SEND_COMMAND: str
SERVICE_SET_FAN_SPEED: str
SERVICE_START_PAUSE: str
SERVICE_START: str
SERVICE_PAUSE: str
SERVICE_STOP: str
STATES: Incomplete
DEFAULT_NAME: str

class VacuumEntityFeature(IntFlag):
    TURN_ON = 1
    TURN_OFF = 2
    PAUSE = 4
    STOP = 8
    RETURN_HOME = 16
    FAN_SPEED = 32
    BATTERY = 64
    STATUS = 128
    SEND_COMMAND = 256
    LOCATE = 512
    CLEAN_SPOT = 1024
    MAP = 2048
    STATE = 4096
    START = 8192

_DEPRECATED_SUPPORT_TURN_ON: Incomplete
_DEPRECATED_SUPPORT_TURN_OFF: Incomplete
_DEPRECATED_SUPPORT_PAUSE: Incomplete
_DEPRECATED_SUPPORT_STOP: Incomplete
_DEPRECATED_SUPPORT_RETURN_HOME: Incomplete
_DEPRECATED_SUPPORT_FAN_SPEED: Incomplete
_DEPRECATED_SUPPORT_BATTERY: Incomplete
_DEPRECATED_SUPPORT_STATUS: Incomplete
_DEPRECATED_SUPPORT_SEND_COMMAND: Incomplete
_DEPRECATED_SUPPORT_LOCATE: Incomplete
_DEPRECATED_SUPPORT_CLEAN_SPOT: Incomplete
_DEPRECATED_SUPPORT_MAP: Incomplete
_DEPRECATED_SUPPORT_STATE: Incomplete
_DEPRECATED_SUPPORT_START: Incomplete

def is_on(hass: HomeAssistant, entity_id: str) -> bool: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class StateVacuumEntityDescription(EntityDescription, frozen_or_thawed=True):
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=...) -> None: ...
    def __replace__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=...) -> None: ...

STATE_VACUUM_CACHED_PROPERTIES_WITH_ATTR_: Incomplete

class StateVacuumEntity(Entity, cached_properties=STATE_VACUUM_CACHED_PROPERTIES_WITH_ATTR_):
    entity_description: StateVacuumEntityDescription
    _entity_component_unrecorded_attributes: Incomplete
    _attr_battery_icon: str
    _attr_battery_level: int | None
    _attr_fan_speed: str | None
    _attr_fan_speed_list: list[str]
    _attr_state: str | None
    _attr_supported_features: VacuumEntityFeature
    def battery_level(self) -> int | None: ...
    @property
    def battery_icon(self) -> str: ...
    @property
    def capability_attributes(self) -> dict[str, Any] | None: ...
    def fan_speed(self) -> str | None: ...
    def fan_speed_list(self) -> list[str]: ...
    @property
    def state_attributes(self) -> dict[str, Any]: ...
    def state(self) -> str | None: ...
    def supported_features(self) -> VacuumEntityFeature: ...
    @property
    def supported_features_compat(self) -> VacuumEntityFeature: ...
    def stop(self, **kwargs: Any) -> None: ...
    async def async_stop(self, **kwargs: Any) -> None: ...
    def return_to_base(self, **kwargs: Any) -> None: ...
    async def async_return_to_base(self, **kwargs: Any) -> None: ...
    def clean_spot(self, **kwargs: Any) -> None: ...
    async def async_clean_spot(self, **kwargs: Any) -> None: ...
    def locate(self, **kwargs: Any) -> None: ...
    async def async_locate(self, **kwargs: Any) -> None: ...
    def set_fan_speed(self, fan_speed: str, **kwargs: Any) -> None: ...
    async def async_set_fan_speed(self, fan_speed: str, **kwargs: Any) -> None: ...
    def send_command(self, command: str, params: dict[str, Any] | list[Any] | None = None, **kwargs: Any) -> None: ...
    async def async_send_command(self, command: str, params: dict[str, Any] | list[Any] | None = None, **kwargs: Any) -> None: ...
    def start(self) -> None: ...
    async def async_start(self) -> None: ...
    def pause(self) -> None: ...
    async def async_pause(self) -> None: ...

__getattr__: Incomplete
__dir__: Incomplete
__all__: Incomplete

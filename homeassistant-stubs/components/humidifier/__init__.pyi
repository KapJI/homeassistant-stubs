from .const import ATTR_ACTION as ATTR_ACTION, ATTR_AVAILABLE_MODES as ATTR_AVAILABLE_MODES, ATTR_CURRENT_HUMIDITY as ATTR_CURRENT_HUMIDITY, ATTR_HUMIDITY as ATTR_HUMIDITY, ATTR_MAX_HUMIDITY as ATTR_MAX_HUMIDITY, ATTR_MIN_HUMIDITY as ATTR_MIN_HUMIDITY, DEFAULT_MAX_HUMIDITY as DEFAULT_MAX_HUMIDITY, DEFAULT_MIN_HUMIDITY as DEFAULT_MIN_HUMIDITY, DOMAIN as DOMAIN, HumidifierAction as HumidifierAction, HumidifierEntityFeature as HumidifierEntityFeature, MODE_AUTO as MODE_AUTO, MODE_AWAY as MODE_AWAY, MODE_BABY as MODE_BABY, MODE_BOOST as MODE_BOOST, MODE_COMFORT as MODE_COMFORT, MODE_ECO as MODE_ECO, MODE_HOME as MODE_HOME, MODE_NORMAL as MODE_NORMAL, MODE_SLEEP as MODE_SLEEP, SERVICE_SET_HUMIDITY as SERVICE_SET_HUMIDITY, SERVICE_SET_MODE as SERVICE_SET_MODE, _DEPRECATED_DEVICE_CLASS_DEHUMIDIFIER as _DEPRECATED_DEVICE_CLASS_DEHUMIDIFIER, _DEPRECATED_DEVICE_CLASS_HUMIDIFIER as _DEPRECATED_DEVICE_CLASS_HUMIDIFIER, _DEPRECATED_SUPPORT_MODES as _DEPRECATED_SUPPORT_MODES
from _typeshed import Incomplete
from enum import StrEnum
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_MODE as ATTR_MODE, SERVICE_TOGGLE as SERVICE_TOGGLE, SERVICE_TURN_OFF as SERVICE_TURN_OFF, SERVICE_TURN_ON as SERVICE_TURN_ON, STATE_ON as STATE_ON
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall
from homeassistant.exceptions import ServiceValidationError as ServiceValidationError
from homeassistant.helpers.deprecation import all_with_deprecated_constants as all_with_deprecated_constants, check_if_deprecated_constant as check_if_deprecated_constant, dir_with_deprecated_constants as dir_with_deprecated_constants
from homeassistant.helpers.entity import ToggleEntity as ToggleEntity, ToggleEntityDescription as ToggleEntityDescription
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.loader import bind_hass as bind_hass
from homeassistant.util.hass_dict import HassKey as HassKey
from typing import Any

_LOGGER: Incomplete
DATA_COMPONENT: HassKey[EntityComponent[HumidifierEntity]]
ENTITY_ID_FORMAT: Incomplete
PLATFORM_SCHEMA: Incomplete
PLATFORM_SCHEMA_BASE: Incomplete
SCAN_INTERVAL: Incomplete

class HumidifierDeviceClass(StrEnum):
    HUMIDIFIER = 'humidifier'
    DEHUMIDIFIER = 'dehumidifier'

DEVICE_CLASSES_SCHEMA: Incomplete
DEVICE_CLASSES: Incomplete

def is_on(hass: HomeAssistant, entity_id: str) -> bool: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class HumidifierEntityDescription(ToggleEntityDescription, frozen_or_thawed=True):
    device_class: HumidifierDeviceClass | None
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=...) -> None: ...
    def __replace__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=...) -> None: ...

CACHED_PROPERTIES_WITH_ATTR_: Incomplete

class HumidifierEntity(ToggleEntity, cached_properties=CACHED_PROPERTIES_WITH_ATTR_):
    _entity_component_unrecorded_attributes: Incomplete
    entity_description: HumidifierEntityDescription
    _attr_action: HumidifierAction | None
    _attr_available_modes: list[str] | None
    _attr_current_humidity: float | None
    _attr_device_class: HumidifierDeviceClass | None
    _attr_max_humidity: float
    _attr_min_humidity: float
    _attr_mode: str | None
    _attr_supported_features: HumidifierEntityFeature
    _attr_target_humidity: float | None
    @property
    def capability_attributes(self) -> dict[str, Any]: ...
    def device_class(self) -> HumidifierDeviceClass | None: ...
    @property
    def state_attributes(self) -> dict[str, Any]: ...
    def action(self) -> HumidifierAction | None: ...
    def current_humidity(self) -> float | None: ...
    def target_humidity(self) -> float | None: ...
    def mode(self) -> str | None: ...
    def available_modes(self) -> list[str] | None: ...
    def set_humidity(self, humidity: int) -> None: ...
    async def async_set_humidity(self, humidity: int) -> None: ...
    def set_mode(self, mode: str) -> None: ...
    async def async_set_mode(self, mode: str) -> None: ...
    def min_humidity(self) -> float: ...
    def max_humidity(self) -> float: ...
    def supported_features(self) -> HumidifierEntityFeature: ...
    @property
    def supported_features_compat(self) -> HumidifierEntityFeature: ...

async def async_service_humidity_set(entity: HumidifierEntity, service_call: ServiceCall) -> None: ...

__getattr__: Incomplete
__dir__: Incomplete
__all__: Incomplete

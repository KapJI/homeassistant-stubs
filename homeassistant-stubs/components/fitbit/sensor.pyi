from .api import FitbitApi as FitbitApi
from .const import ATTRIBUTION as ATTRIBUTION, ATTR_ACCESS_TOKEN as ATTR_ACCESS_TOKEN, ATTR_LAST_SAVED_AT as ATTR_LAST_SAVED_AT, ATTR_REFRESH_TOKEN as ATTR_REFRESH_TOKEN, BATTERY_LEVELS as BATTERY_LEVELS, CONF_CLOCK_FORMAT as CONF_CLOCK_FORMAT, CONF_MONITORED_RESOURCES as CONF_MONITORED_RESOURCES, DEFAULT_CLOCK_FORMAT as DEFAULT_CLOCK_FORMAT, DEFAULT_CONFIG as DEFAULT_CONFIG, DOMAIN as DOMAIN, FITBIT_CONFIG_FILE as FITBIT_CONFIG_FILE, FITBIT_DEFAULT_RESOURCES as FITBIT_DEFAULT_RESOURCES, FitbitScope as FitbitScope, FitbitUnitSystem as FitbitUnitSystem
from .coordinator import FitbitData as FitbitData, FitbitDeviceCoordinator as FitbitDeviceCoordinator
from .exceptions import FitbitApiException as FitbitApiException, FitbitAuthException as FitbitAuthException
from .model import FitbitDevice as FitbitDevice, config_from_entry_data as config_from_entry_data
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.application_credentials import ClientCredential as ClientCredential, async_import_client_credential as async_import_client_credential
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry, SOURCE_IMPORT as SOURCE_IMPORT
from homeassistant.const import CONF_CLIENT_ID as CONF_CLIENT_ID, CONF_CLIENT_SECRET as CONF_CLIENT_SECRET, CONF_TOKEN as CONF_TOKEN, CONF_UNIT_SYSTEM as CONF_UNIT_SYSTEM, EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, UnitOfLength as UnitOfLength, UnitOfMass as UnitOfMass, UnitOfTime as UnitOfTime, UnitOfVolume as UnitOfVolume
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.data_entry_flow import FlowResultType as FlowResultType
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.icon import icon_for_battery_level as icon_for_battery_level
from homeassistant.helpers.issue_registry import IssueSeverity as IssueSeverity, async_create_issue as async_create_issue
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from homeassistant.util.json import load_json_object as load_json_object
from typing import Any, Final

_LOGGER: Final[Incomplete]
_CONFIGURING: dict[str, str]
SCAN_INTERVAL: Final[Incomplete]

def _default_value_fn(result: dict[str, Any]) -> str: ...
def _distance_value_fn(result: dict[str, Any]) -> int | str: ...
def _body_value_fn(result: dict[str, Any]) -> int | str: ...
def _clock_format_12h(result: dict[str, Any]) -> str: ...
def _weight_unit(unit_system: FitbitUnitSystem) -> UnitOfMass: ...
def _distance_unit(unit_system: FitbitUnitSystem) -> UnitOfLength: ...
def _elevation_unit(unit_system: FitbitUnitSystem) -> UnitOfLength: ...
def _water_unit(unit_system: FitbitUnitSystem) -> UnitOfVolume: ...
def _int_value_or_none(field: str) -> Callable[[dict[str, Any]], int | None]: ...

@dataclass(frozen=True)
class FitbitSensorEntityDescription(SensorEntityDescription):
    unit_type: str | None = ...
    value_fn: Callable[[dict[str, Any]], Any] = ...
    unit_fn: Callable[[FitbitUnitSystem], str | None] = ...
    scope: FitbitScope | None = ...
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=..., last_reset=..., native_unit_of_measurement=..., options=..., state_class=..., suggested_display_precision=..., suggested_unit_of_measurement=..., unit_type=..., value_fn=..., unit_fn=..., scope=...) -> None: ...

FITBIT_RESOURCES_LIST: Final[tuple[FitbitSensorEntityDescription, ...]]
SLEEP_START_TIME: Incomplete
SLEEP_START_TIME_12HR: Incomplete
FITBIT_RESOURCE_BATTERY: Incomplete
FITBIT_RESOURCE_BATTERY_LEVEL: Incomplete
FITBIT_RESOURCES_KEYS: Final[list[str]]
PLATFORM_SCHEMA: Final[Incomplete]
FITBIT_CONF_KEYS: Incomplete

def load_config_file(config_path: str) -> dict[str, Any] | None: ...
async def async_setup_platform(hass: HomeAssistant, config: ConfigType, add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class FitbitSensor(SensorEntity):
    entity_description: FitbitSensorEntityDescription
    _attr_attribution = ATTRIBUTION
    config_entry: Incomplete
    api: Incomplete
    _attr_unique_id: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    _attr_entity_registry_enabled_default: bool
    def __init__(self, config_entry: ConfigEntry, api: FitbitApi, user_profile_id: str, description: FitbitSensorEntityDescription, units: str | None, enable_default_override: bool) -> None: ...
    _attr_available: bool
    _attr_native_value: Incomplete
    async def async_update(self) -> None: ...
    async def async_added_to_hass(self) -> None: ...

class FitbitBatterySensor(CoordinatorEntity[FitbitDeviceCoordinator], SensorEntity):
    entity_description: FitbitSensorEntityDescription
    _attr_attribution = ATTRIBUTION
    device: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    _attr_entity_registry_enabled_default: bool
    def __init__(self, coordinator: FitbitDeviceCoordinator, user_profile_id: str, description: FitbitSensorEntityDescription, device: FitbitDevice, enable_default_override: bool) -> None: ...
    @property
    def icon(self) -> str | None: ...
    @property
    def extra_state_attributes(self) -> dict[str, str | None]: ...
    async def async_added_to_hass(self) -> None: ...
    _attr_native_value: Incomplete
    def _handle_coordinator_update(self) -> None: ...

class FitbitBatteryLevelSensor(CoordinatorEntity[FitbitDeviceCoordinator], SensorEntity):
    entity_description: FitbitSensorEntityDescription
    _attr_attribution = ATTRIBUTION
    device: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: FitbitDeviceCoordinator, user_profile_id: str, description: FitbitSensorEntityDescription, device: FitbitDevice) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    _attr_native_value: Incomplete
    def _handle_coordinator_update(self) -> None: ...

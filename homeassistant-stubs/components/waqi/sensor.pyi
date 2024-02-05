from .const import CONF_STATION_NUMBER as CONF_STATION_NUMBER, DOMAIN as DOMAIN, ISSUE_PLACEHOLDER as ISSUE_PLACEHOLDER
from .coordinator import WAQIDataUpdateCoordinator as WAQIDataUpdateCoordinator
from _typeshed import Incomplete
from aiowaqi import WAQIAirQuality as WAQIAirQuality
from collections.abc import Callable as Callable, Mapping
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry, SOURCE_IMPORT as SOURCE_IMPORT
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, ATTR_TIME as ATTR_TIME, CONF_API_KEY as CONF_API_KEY, CONF_NAME as CONF_NAME, CONF_TOKEN as CONF_TOKEN, PERCENTAGE as PERCENTAGE, UnitOfPressure as UnitOfPressure, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import PlatformNotReady as PlatformNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.issue_registry import IssueSeverity as IssueSeverity, async_create_issue as async_create_issue
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType, StateType as StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

_LOGGER: Incomplete
ATTR_DOMINENTPOL: str
ATTR_HUMIDITY: str
ATTR_NITROGEN_DIOXIDE: str
ATTR_OZONE: str
ATTR_PM10: str
ATTR_PM2_5: str
ATTR_PRESSURE: str
ATTR_SULFUR_DIOXIDE: str
ATTRIBUTION: str
ATTR_ICON: str
CONF_LOCATIONS: str
CONF_STATIONS: str
TIMEOUT: int
PLATFORM_SCHEMA: Incomplete

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...

@dataclass(frozen=True)
class WAQIMixin:
    available_fn: Callable[[WAQIAirQuality], bool]
    value_fn: Callable[[WAQIAirQuality], StateType]
    def __init__(self, available_fn, value_fn) -> None: ...

@dataclass(frozen=True)
class WAQISensorEntityDescription(SensorEntityDescription, WAQIMixin):
    def __init__(self, available_fn, value_fn, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, last_reset, native_unit_of_measurement, options, state_class, suggested_display_precision, suggested_unit_of_measurement) -> None: ...

SENSORS: list[WAQISensorEntityDescription]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class WaqiSensor(CoordinatorEntity[WAQIDataUpdateCoordinator], SensorEntity):
    _attr_has_entity_name: bool
    entity_description: WAQISensorEntityDescription
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    _attr_attribution: Incomplete
    def __init__(self, coordinator: WAQIDataUpdateCoordinator, entity_description: WAQISensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> StateType: ...
    @property
    def extra_state_attributes(self) -> Mapping[str, Any] | None: ...

from .const import DOMAIN as DOMAIN, INTEGRATION_TITLE as INTEGRATION_TITLE
from .coordinator import OpenEVSEConfigEntry as OpenEVSEConfigEntry, OpenEVSEDataUpdateCoordinator as OpenEVSEDataUpdateCoordinator
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import SOURCE_IMPORT as SOURCE_IMPORT
from homeassistant.const import ATTR_CONNECTIONS as ATTR_CONNECTIONS, ATTR_SERIAL_NUMBER as ATTR_SERIAL_NUMBER, CONF_HOST as CONF_HOST, CONF_MONITORED_VARIABLES as CONF_MONITORED_VARIABLES, EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, SIGNAL_STRENGTH_DECIBELS as SIGNAL_STRENGTH_DECIBELS, UnitOfElectricCurrent as UnitOfElectricCurrent, UnitOfElectricPotential as UnitOfElectricPotential, UnitOfEnergy as UnitOfEnergy, UnitOfInformation as UnitOfInformation, UnitOfLength as UnitOfLength, UnitOfPower as UnitOfPower, UnitOfTemperature as UnitOfTemperature, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.data_entry_flow import FlowResultType as FlowResultType
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback, AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType, StateType as StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from openevsehttp.__main__ import OpenEVSE as OpenEVSE

_LOGGER: Incomplete
PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class OpenEVSESensorDescription(SensorEntityDescription):
    value_fn: Callable[[OpenEVSE], str | float | datetime | None]

SENSOR_TYPES: tuple[OpenEVSESensorDescription, ...]
SENSOR_KEYS: list[str]
PLATFORM_SCHEMA: Incomplete

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...
async def async_setup_entry(hass: HomeAssistant, entry: OpenEVSEConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class OpenEVSESensor(CoordinatorEntity[OpenEVSEDataUpdateCoordinator], SensorEntity):
    _attr_has_entity_name: bool
    entity_description: OpenEVSESensorDescription
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: OpenEVSEDataUpdateCoordinator, description: OpenEVSESensorDescription, identifier: str, unique_id: str | None) -> None: ...
    @property
    def native_value(self) -> StateType | datetime: ...

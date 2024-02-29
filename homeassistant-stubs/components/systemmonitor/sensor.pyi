from .const import CONF_PROCESS as CONF_PROCESS, DOMAIN as DOMAIN, DOMAIN_COORDINATORS as DOMAIN_COORDINATORS, NET_IO_TYPES as NET_IO_TYPES
from .coordinator import MonitorCoordinator as MonitorCoordinator, SystemMonitorBootTimeCoordinator as SystemMonitorBootTimeCoordinator, SystemMonitorCPUtempCoordinator as SystemMonitorCPUtempCoordinator, SystemMonitorDiskCoordinator as SystemMonitorDiskCoordinator, SystemMonitorLoadCoordinator as SystemMonitorLoadCoordinator, SystemMonitorMemoryCoordinator as SystemMonitorMemoryCoordinator, SystemMonitorNetAddrCoordinator as SystemMonitorNetAddrCoordinator, SystemMonitorNetIOCoordinator as SystemMonitorNetIOCoordinator, SystemMonitorProcessCoordinator as SystemMonitorProcessCoordinator, SystemMonitorProcessorCoordinator as SystemMonitorProcessorCoordinator, SystemMonitorSwapCoordinator as SystemMonitorSwapCoordinator, VirtualMemory as VirtualMemory, dataT as dataT
from .util import get_all_disk_mounts as get_all_disk_mounts, get_all_network_interfaces as get_all_network_interfaces, read_cpu_temperature as read_cpu_temperature
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from datetime import datetime
from homeassistant.components.sensor import PLATFORM_SCHEMA as PLATFORM_SCHEMA, SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry, SOURCE_IMPORT as SOURCE_IMPORT
from homeassistant.const import CONF_RESOURCES as CONF_RESOURCES, CONF_TYPE as CONF_TYPE, EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, STATE_OFF as STATE_OFF, STATE_ON as STATE_ON, UnitOfDataRate as UnitOfDataRate, UnitOfInformation as UnitOfInformation, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.issue_registry import IssueSeverity as IssueSeverity, async_create_issue as async_create_issue
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType, StateType as StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from homeassistant.util import slugify as slugify
from psutil import Process
from psutil._common import shwtemp, snetio, snicaddr
from typing import Any, Generic, Literal

_LOGGER: Incomplete
CONF_ARG: str
SENSOR_TYPE_NAME: int
SENSOR_TYPE_UOM: int
SENSOR_TYPE_ICON: int
SENSOR_TYPE_DEVICE_CLASS: int
SENSOR_TYPE_MANDATORY_ARG: int
SIGNAL_SYSTEMMONITOR_UPDATE: str

def get_cpu_icon() -> Literal['mdi:cpu-64-bit', 'mdi:cpu-32-bit']: ...
def get_processor_temperature(entity: SystemMonitorSensor[dict[str, list[shwtemp]]]) -> float | None: ...
def get_process(entity: SystemMonitorSensor[list[Process]]) -> str: ...
def get_network(entity: SystemMonitorSensor[dict[str, snetio]]) -> float | None: ...
def get_packets(entity: SystemMonitorSensor[dict[str, snetio]]) -> float | None: ...
def get_throughput(entity: SystemMonitorSensor[dict[str, snetio]]) -> float | None: ...
def get_ip_address(entity: SystemMonitorSensor[dict[str, list[snicaddr]]]) -> str | None: ...

@dataclass(frozen=True, kw_only=True)
class SysMonitorSensorEntityDescription(SensorEntityDescription, Generic[dataT]):
    value_fn: Callable[[SystemMonitorSensor[dataT]], StateType | datetime]
    mandatory_arg: bool = ...
    placeholder: str | None = ...
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, last_reset, native_unit_of_measurement, options, state_class, suggested_display_precision, suggested_unit_of_measurement, value_fn, mandatory_arg, placeholder) -> None: ...

SENSOR_TYPES: dict[str, SysMonitorSensorEntityDescription[Any]]

def check_required_arg(value: Any) -> Any: ...
def check_legacy_resource(resource: str, resources: set[str]) -> bool: ...

IO_COUNTER: Incomplete
IF_ADDRS_FAMILY: Incomplete

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SystemMonitorSensor(CoordinatorEntity[MonitorCoordinator[dataT]], SensorEntity):
    _attr_has_entity_name: bool
    _attr_entity_category: Incomplete
    entity_description: SysMonitorSensorEntityDescription[dataT]
    _attr_translation_placeholders: Incomplete
    _attr_unique_id: Incomplete
    _attr_entity_registry_enabled_default: Incomplete
    _attr_device_info: Incomplete
    argument: Incomplete
    value: Incomplete
    update_time: Incomplete
    def __init__(self, coordinator: MonitorCoordinator[dataT], sensor_description: SysMonitorSensorEntityDescription[dataT], entry_id: str, argument: str, legacy_enabled: bool = False) -> None: ...
    @property
    def native_value(self) -> StateType | datetime: ...

from .const import CONF_PROCESS as CONF_PROCESS, DOMAIN as DOMAIN
from .coordinator import MonitorCoordinator as MonitorCoordinator, SystemMonitorProcessCoordinator as SystemMonitorProcessCoordinator, dataT as dataT
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from homeassistant.util import slugify as slugify
from psutil import Process
from typing import Generic, Literal

_LOGGER: Incomplete
CONF_ARG: str
SENSOR_TYPE_NAME: int
SENSOR_TYPE_UOM: int
SENSOR_TYPE_ICON: int
SENSOR_TYPE_DEVICE_CLASS: int
SENSOR_TYPE_MANDATORY_ARG: int
SIGNAL_SYSTEMMONITOR_UPDATE: str

def get_cpu_icon() -> Literal['mdi:cpu-64-bit', 'mdi:cpu-32-bit']: ...
def get_process(entity: SystemMonitorSensor[list[Process]]) -> bool: ...

@dataclass(frozen=True, kw_only=True)
class SysMonitorBinarySensorEntityDescription(BinarySensorEntityDescription, Generic[dataT]):
    value_fn: Callable[[SystemMonitorSensor[dataT]], bool]
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, value_fn) -> None: ...

SENSOR_TYPES: tuple[SysMonitorBinarySensorEntityDescription[list[Process]], ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SystemMonitorSensor(CoordinatorEntity[MonitorCoordinator[dataT]], BinarySensorEntity):
    _attr_has_entity_name: bool
    _attr_entity_category: Incomplete
    entity_description: SysMonitorBinarySensorEntityDescription[dataT]
    _attr_translation_placeholders: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    argument: Incomplete
    def __init__(self, coordinator: MonitorCoordinator[dataT], sensor_description: SysMonitorBinarySensorEntityDescription[dataT], entry_id: str, argument: str) -> None: ...
    @property
    def is_on(self) -> bool | None: ...

from .const import DOMAIN as DOMAIN, HAS_CERT as HAS_CERT, HAS_HOST as HAS_HOST, HAS_PORT as HAS_PORT, HAS_URL as HAS_URL, LOCAL_INSTANCE as LOCAL_INSTANCE
from .coordinator import UptimeKumaConfigEntry as UptimeKumaConfigEntry, UptimeKumaDataUpdateCoordinator as UptimeKumaDataUpdateCoordinator
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Mapping
from dataclasses import dataclass
from enum import StrEnum
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import CONF_URL as CONF_URL, EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from pythonkuma import MonitorType, UptimeKumaMonitor as UptimeKumaMonitor
from typing import Any

PARALLEL_UPDATES: int

class UptimeKumaSensor(StrEnum):
    CERT_DAYS_REMAINING = 'cert_days_remaining'
    RESPONSE_TIME = 'response_time'
    STATUS = 'status'
    TYPE = 'type'
    URL = 'url'
    HOSTNAME = 'hostname'
    PORT = 'port'
    UPTIME_RATIO_1D = 'uptime_1d'
    UPTIME_RATIO_30D = 'uptime_30d'
    UPTIME_RATIO_365D = 'uptime_365d'
    AVG_RESPONSE_TIME_1D = 'avg_response_time_1d'
    AVG_RESPONSE_TIME_30D = 'avg_response_time_30d'
    AVG_RESPONSE_TIME_365D = 'avg_response_time_365d'
    TAGS = 'tags'

@dataclass(kw_only=True, frozen=True)
class UptimeKumaSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[UptimeKumaMonitor], StateType]
    create_entity: Callable[[MonitorType], bool]
    attributes_fn: Callable[[UptimeKumaMonitor], Mapping[str, Any]] | None = ...

SENSOR_DESCRIPTIONS: tuple[UptimeKumaSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: UptimeKumaConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class UptimeKumaSensorEntity(CoordinatorEntity[UptimeKumaDataUpdateCoordinator], SensorEntity):
    entity_description: UptimeKumaSensorEntityDescription
    _attr_has_entity_name: bool
    monitor: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: UptimeKumaDataUpdateCoordinator, monitor: str | int, entity_description: UptimeKumaSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> StateType: ...
    @property
    def available(self) -> bool: ...
    @property
    def extra_state_attributes(self) -> Mapping[str, Any] | None: ...

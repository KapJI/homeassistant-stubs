from .const import CONNECTED_PLC_DEVICES as CONNECTED_PLC_DEVICES, CONNECTED_WIFI_CLIENTS as CONNECTED_WIFI_CLIENTS, DOMAIN as DOMAIN, NEIGHBORING_WIFI_NETWORKS as NEIGHBORING_WIFI_NETWORKS, PLC_RX_RATE as PLC_RX_RATE, PLC_TX_RATE as PLC_TX_RATE
from .entity import DevoloCoordinatorEntity as DevoloCoordinatorEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from devolo_plc_api.device import Device as Device
from devolo_plc_api.device_api import ConnectedStationInfo, NeighborAPInfo
from devolo_plc_api.plcnet_api import DataRate, LogicalNetwork
from enum import StrEnum
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory, UnitOfDataRate as UnitOfDataRate
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from typing import Any, Generic, TypeVar

_CoordinatorDataT = TypeVar('_CoordinatorDataT', bound=LogicalNetwork | DataRate | list[ConnectedStationInfo] | list[NeighborAPInfo])
_ValueDataT = TypeVar('_ValueDataT', bound=LogicalNetwork | DataRate | list[ConnectedStationInfo] | list[NeighborAPInfo])

class DataRateDirection(StrEnum):
    RX: str
    TX: str

@dataclass(frozen=True)
class DevoloSensorRequiredKeysMixin(Generic[_CoordinatorDataT]):
    value_func: Callable[[_CoordinatorDataT], float]
    def __init__(self, value_func) -> None: ...

@dataclass(frozen=True)
class DevoloSensorEntityDescription(SensorEntityDescription, DevoloSensorRequiredKeysMixin[_CoordinatorDataT]):
    def __init__(self, value_func, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, last_reset, native_unit_of_measurement, options, state_class, suggested_display_precision, suggested_unit_of_measurement) -> None: ...

SENSOR_TYPES: dict[str, DevoloSensorEntityDescription[Any]]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class BaseDevoloSensorEntity(DevoloCoordinatorEntity[_CoordinatorDataT], SensorEntity, Generic[_CoordinatorDataT, _ValueDataT]):
    entity_description: Incomplete
    def __init__(self, entry: ConfigEntry, coordinator: DataUpdateCoordinator[_CoordinatorDataT], description: DevoloSensorEntityDescription[_ValueDataT], device: Device) -> None: ...

class DevoloSensorEntity(BaseDevoloSensorEntity[_CoordinatorDataT, _CoordinatorDataT]):
    entity_description: DevoloSensorEntityDescription[_CoordinatorDataT]
    @property
    def native_value(self) -> float: ...

class DevoloPlcDataRateSensorEntity(BaseDevoloSensorEntity[LogicalNetwork, DataRate]):
    entity_description: DevoloSensorEntityDescription[DataRate]
    _peer: Incomplete
    _attr_unique_id: Incomplete
    _attr_name: Incomplete
    _attr_entity_registry_enabled_default: Incomplete
    def __init__(self, entry: ConfigEntry, coordinator: DataUpdateCoordinator[LogicalNetwork], description: DevoloSensorEntityDescription[DataRate], device: Device, peer: str) -> None: ...
    @property
    def native_value(self) -> float: ...

from . import DevoloHomeNetworkConfigEntry as DevoloHomeNetworkConfigEntry
from .const import CONNECTED_PLC_DEVICES as CONNECTED_PLC_DEVICES, CONNECTED_WIFI_CLIENTS as CONNECTED_WIFI_CLIENTS, LAST_RESTART as LAST_RESTART, NEIGHBORING_WIFI_NETWORKS as NEIGHBORING_WIFI_NETWORKS, PLC_RX_RATE as PLC_RX_RATE, PLC_TX_RATE as PLC_TX_RATE
from .entity import DevoloCoordinatorEntity as DevoloCoordinatorEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from datetime import datetime
from devolo_plc_api.device_api import ConnectedStationInfo, NeighborAPInfo
from devolo_plc_api.plcnet_api import DataRate, LogicalNetwork
from enum import StrEnum
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, UnitOfDataRate as UnitOfDataRate
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from homeassistant.util.dt import utcnow as utcnow
from typing import Any, Generic, TypeVar

PARALLEL_UPDATES: int

def _last_restart(runtime: int) -> datetime: ...
_CoordinatorDataT = TypeVar('_CoordinatorDataT', bound=LogicalNetwork | DataRate | list[ConnectedStationInfo] | list[NeighborAPInfo] | int)
_ValueDataT = TypeVar('_ValueDataT', bound=LogicalNetwork | DataRate | list[ConnectedStationInfo] | list[NeighborAPInfo] | int)
_SensorDataT = TypeVar('_SensorDataT', bound=int | float | datetime)

class DataRateDirection(StrEnum):
    RX = 'rx_rate'
    TX = 'tx_rate'

@dataclass(frozen=True, kw_only=True)
class DevoloSensorEntityDescription(SensorEntityDescription, Generic[_CoordinatorDataT, _SensorDataT]):
    value_func: Callable[[_CoordinatorDataT], _SensorDataT]
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=..., last_reset=..., native_unit_of_measurement=..., options=..., state_class=..., suggested_display_precision=..., suggested_unit_of_measurement=..., value_func) -> None: ...

SENSOR_TYPES: dict[str, DevoloSensorEntityDescription[Any, Any]]

async def async_setup_entry(hass: HomeAssistant, entry: DevoloHomeNetworkConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class BaseDevoloSensorEntity(DevoloCoordinatorEntity[_CoordinatorDataT], SensorEntity, Generic[_CoordinatorDataT, _ValueDataT, _SensorDataT]):
    entity_description: Incomplete
    def __init__(self, entry: DevoloHomeNetworkConfigEntry, coordinator: DataUpdateCoordinator[_CoordinatorDataT], description: DevoloSensorEntityDescription[_ValueDataT, _SensorDataT]) -> None: ...

class DevoloSensorEntity(BaseDevoloSensorEntity[_CoordinatorDataT, _CoordinatorDataT, _SensorDataT]):
    entity_description: DevoloSensorEntityDescription[_CoordinatorDataT, _SensorDataT]
    @property
    def native_value(self) -> int | float | datetime: ...

class DevoloPlcDataRateSensorEntity(BaseDevoloSensorEntity[LogicalNetwork, DataRate, float]):
    entity_description: DevoloSensorEntityDescription[DataRate, float]
    _peer: Incomplete
    _attr_unique_id: Incomplete
    _attr_name: Incomplete
    _attr_entity_registry_enabled_default: Incomplete
    def __init__(self, entry: DevoloHomeNetworkConfigEntry, coordinator: DataUpdateCoordinator[LogicalNetwork], description: DevoloSensorEntityDescription[DataRate, float], peer: str) -> None: ...
    @property
    def native_value(self) -> float: ...

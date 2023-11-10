from .const import CONNECTED_PLC_DEVICES as CONNECTED_PLC_DEVICES, CONNECTED_WIFI_CLIENTS as CONNECTED_WIFI_CLIENTS, DOMAIN as DOMAIN, NEIGHBORING_WIFI_NETWORKS as NEIGHBORING_WIFI_NETWORKS
from .entity import DevoloCoordinatorEntity as DevoloCoordinatorEntity
from collections.abc import Callable as Callable
from dataclasses import dataclass
from devolo_plc_api.device import Device as Device
from devolo_plc_api.device_api import ConnectedStationInfo, NeighborAPInfo
from devolo_plc_api.plcnet_api import LogicalNetwork
from homeassistant.components.sensor import SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from typing import Any, Generic, TypeVar

_DataT = TypeVar('_DataT', bound=LogicalNetwork | list[ConnectedStationInfo] | list[NeighborAPInfo])

@dataclass
class DevoloSensorRequiredKeysMixin(Generic[_DataT]):
    value_func: Callable[[_DataT], int]
    def __init__(self, value_func) -> None: ...

@dataclass
class DevoloSensorEntityDescription(SensorEntityDescription, DevoloSensorRequiredKeysMixin[_DataT]):
    def __init__(self, value_func, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, last_reset, native_unit_of_measurement, options, state_class, suggested_display_precision, suggested_unit_of_measurement) -> None: ...

SENSOR_TYPES: dict[str, DevoloSensorEntityDescription[Any]]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DevoloSensorEntity(DevoloCoordinatorEntity[_DataT], SensorEntity):
    entity_description: DevoloSensorEntityDescription[_DataT]
    def __init__(self, entry: ConfigEntry, coordinator: DataUpdateCoordinator[_DataT], description: DevoloSensorEntityDescription[_DataT], device: Device) -> None: ...
    @property
    def native_value(self) -> int: ...

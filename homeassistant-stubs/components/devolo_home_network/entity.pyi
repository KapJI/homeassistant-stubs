from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from devolo_plc_api.device import Device as Device
from devolo_plc_api.device_api import ConnectedStationInfo, NeighborAPInfo, WifiGuestAccessGet
from devolo_plc_api.plcnet_api import LogicalNetwork
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator
from typing import TypeVar

_DataT = TypeVar('_DataT', bound=LogicalNetwork | list[ConnectedStationInfo] | list[NeighborAPInfo] | WifiGuestAccessGet | bool)

class DevoloEntity(Entity):
    _attr_has_entity_name: bool
    device: Incomplete
    entry: Incomplete
    _attr_device_info: Incomplete
    _attr_translation_key: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, entry: ConfigEntry, device: Device) -> None: ...

class DevoloCoordinatorEntity(CoordinatorEntity[DataUpdateCoordinator[_DataT]], DevoloEntity):
    def __init__(self, entry: ConfigEntry, coordinator: DataUpdateCoordinator[_DataT], device: Device) -> None: ...

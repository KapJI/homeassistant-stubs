import abc
from .const import DOMAIN as DOMAIN
from .coordinator import SMHIDataUpdateCoordinator as SMHIDataUpdateCoordinator
from _typeshed import Incomplete
from abc import abstractmethod
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class SmhiWeatherBaseEntity(CoordinatorEntity[SMHIDataUpdateCoordinator], metaclass=abc.ABCMeta):
    _attr_attribution: str
    _attr_has_entity_name: bool
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, latitude: str, longitude: str, coordinator: SMHIDataUpdateCoordinator) -> None: ...
    @abstractmethod
    def update_entity_data(self) -> None: ...

import abc
from .const import DOMAIN as DOMAIN
from .coordinator import SMHIDataUpdateCoordinator as SMHIDataUpdateCoordinator, SMHIFireDataUpdateCoordinator as SMHIFireDataUpdateCoordinator
from _typeshed import Incomplete
from abc import abstractmethod
from homeassistant.core import callback as callback
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class SmhiWeatherBaseEntity(Entity, metaclass=abc.ABCMeta):
    _attr_attribution: str
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, latitude: str, longitude: str) -> None: ...
    @abstractmethod
    def update_entity_data(self) -> None: ...

class SmhiWeatherEntity(CoordinatorEntity[SMHIDataUpdateCoordinator], SmhiWeatherBaseEntity, metaclass=abc.ABCMeta):
    def __init__(self, latitude: str, longitude: str, coordinator: SMHIDataUpdateCoordinator) -> None: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...

class SmhiFireEntity(CoordinatorEntity[SMHIFireDataUpdateCoordinator], SmhiWeatherBaseEntity, metaclass=abc.ABCMeta):
    def __init__(self, latitude: str, longitude: str, coordinator: SMHIFireDataUpdateCoordinator) -> None: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...

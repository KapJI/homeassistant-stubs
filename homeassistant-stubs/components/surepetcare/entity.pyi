import abc
from . import SurePetcareDataCoordinator as SurePetcareDataCoordinator
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from abc import abstractmethod
from homeassistant.core import callback as callback
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from surepy.entities import SurepyEntity as SurepyEntity

class SurePetcareEntity(CoordinatorEntity[SurePetcareDataCoordinator], metaclass=abc.ABCMeta):
    _id: Incomplete
    _device_name: Incomplete
    _device_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, surepetcare_id: int, coordinator: SurePetcareDataCoordinator) -> None: ...
    @abstractmethod
    def _update_attr(self, surepy_entity: SurepyEntity) -> None: ...
    def _handle_coordinator_update(self) -> None: ...

import abc
from . import SurePetcareDataCoordinator as SurePetcareDataCoordinator
from .const import DOMAIN as DOMAIN
from abc import abstractmethod
from homeassistant.core import callback as callback
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from surepy.entities import SurepyEntity as SurepyEntity
from typing import Any

class SurePetcareEntity(CoordinatorEntity, metaclass=abc.ABCMeta):
    _id: Any
    _device_name: Any
    _device_id: Any
    _attr_device_info: Any
    def __init__(self, surepetcare_id: int, coordinator: SurePetcareDataCoordinator) -> None: ...
    @abstractmethod
    def _update_attr(self, surepy_entity: SurepyEntity) -> None: ...
    def _handle_coordinator_update(self) -> None: ...

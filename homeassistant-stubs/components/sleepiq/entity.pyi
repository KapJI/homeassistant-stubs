import abc
from .const import ENTITY_TYPES as ENTITY_TYPES, ICON_OCCUPIED as ICON_OCCUPIED
from _typeshed import Incomplete
from abc import abstractmethod
from asyncsleepiq import SleepIQBed as SleepIQBed, SleepIQSleeper as SleepIQSleeper
from homeassistant.core import callback as callback
from homeassistant.helpers import device_registry as device_registry
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo, Entity as Entity
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator

def device_from_bed(bed: SleepIQBed) -> DeviceInfo: ...

class SleepIQEntity(Entity):
    bed: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, bed: SleepIQBed) -> None: ...

class SleepIQBedEntity(CoordinatorEntity, metaclass=abc.ABCMeta):
    _attr_icon: Incomplete
    bed: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: DataUpdateCoordinator, bed: SleepIQBed) -> None: ...
    def _handle_coordinator_update(self) -> None: ...
    @abstractmethod
    def _async_update_attrs(self) -> None: ...

class SleepIQSleeperEntity(SleepIQBedEntity, metaclass=abc.ABCMeta):
    _attr_icon: Incomplete
    sleeper: Incomplete
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: DataUpdateCoordinator, bed: SleepIQBed, sleeper: SleepIQSleeper, name: str) -> None: ...

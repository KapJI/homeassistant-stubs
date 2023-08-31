import abc
from .const import ENTITY_TYPES as ENTITY_TYPES, ICON_OCCUPIED as ICON_OCCUPIED
from .coordinator import SleepIQDataUpdateCoordinator as SleepIQDataUpdateCoordinator, SleepIQPauseUpdateCoordinator as SleepIQPauseUpdateCoordinator
from _typeshed import Incomplete
from abc import abstractmethod
from asyncsleepiq import SleepIQBed as SleepIQBed, SleepIQSleeper as SleepIQSleeper
from homeassistant.core import callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import TypeVar

_SleepIQCoordinatorT = TypeVar('_SleepIQCoordinatorT', bound=SleepIQDataUpdateCoordinator | SleepIQPauseUpdateCoordinator)

def device_from_bed(bed: SleepIQBed) -> DeviceInfo: ...

class SleepIQEntity(Entity):
    bed: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, bed: SleepIQBed) -> None: ...

class SleepIQBedEntity(CoordinatorEntity[_SleepIQCoordinatorT], metaclass=abc.ABCMeta):
    _attr_icon = ICON_OCCUPIED
    bed: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: _SleepIQCoordinatorT, bed: SleepIQBed) -> None: ...
    def _handle_coordinator_update(self) -> None: ...
    @abstractmethod
    def _async_update_attrs(self) -> None: ...

class SleepIQSleeperEntity(SleepIQBedEntity[_SleepIQCoordinatorT], metaclass=abc.ABCMeta):
    _attr_icon = ICON_OCCUPIED
    sleeper: Incomplete
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: _SleepIQCoordinatorT, bed: SleepIQBed, sleeper: SleepIQSleeper, name: str) -> None: ...

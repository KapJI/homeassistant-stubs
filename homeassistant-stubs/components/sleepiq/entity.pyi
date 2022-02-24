import abc
from .const import ICON_OCCUPIED as ICON_OCCUPIED, SENSOR_TYPES as SENSOR_TYPES
from abc import abstractmethod
from asyncsleepiq import SleepIQBed as SleepIQBed, SleepIQSleeper as SleepIQSleeper
from homeassistant.core import callback as callback
from homeassistant.helpers import device_registry as device_registry
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo, Entity as Entity
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator
from typing import Any

def device_from_bed(bed: SleepIQBed) -> DeviceInfo: ...

class SleepIQEntity(Entity):
    bed: Any
    _attr_device_info: Any
    def __init__(self, bed: SleepIQBed) -> None: ...

class SleepIQSensor(CoordinatorEntity, metaclass=abc.ABCMeta):
    _attr_icon: Any
    sleeper: Any
    bed: Any
    _attr_device_info: Any
    _attr_name: Any
    _attr_unique_id: Any
    def __init__(self, coordinator: DataUpdateCoordinator, bed: SleepIQBed, sleeper: SleepIQSleeper, name: str) -> None: ...
    def _handle_coordinator_update(self) -> None: ...
    @abstractmethod
    def _async_update_attrs(self) -> None: ...

class SleepIQBedCoordinator(CoordinatorEntity):
    _attr_icon: Any
    bed: Any
    _attr_device_info: Any
    def __init__(self, coordinator: DataUpdateCoordinator, bed: SleepIQBed) -> None: ...

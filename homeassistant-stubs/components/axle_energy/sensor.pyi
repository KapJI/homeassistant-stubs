from .coordinator import AxleConfigEntry as AxleConfigEntry, AxleCoordinator as AxleCoordinator
from .entity import AxleEntity as AxleEntity
from _typeshed import Incomplete
from aioaxlevpp import GridEvent as GridEvent
from collections.abc import Callable as Callable
from dataclasses import dataclass
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import override

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class AxleSensorDescription(SensorEntityDescription):
    value_fn: Callable[[GridEvent], str | datetime]

SENSORS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: AxleConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class AxleSensor(AxleEntity, SensorEntity):
    entity_description: AxleSensorDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: AxleCoordinator, description: AxleSensorDescription) -> None: ...
    @property
    @override
    def native_value(self) -> str | datetime | None: ...

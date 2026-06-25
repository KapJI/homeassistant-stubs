from . import PajGpsConfigEntry as PajGpsConfigEntry
from .coordinator import Device as Device, PajGpsCoordinator as PajGpsCoordinator
from .entity import PajGpsEntity as PajGpsEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass, field
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, UnitOfSpeed as UnitOfSpeed
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pajgps_api.models.trackpoint import TrackPoint as TrackPoint
from typing import override

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class PajGpsSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[TrackPoint], int | None]
    supported_fn: Callable[[Device], bool] = field(default=Incomplete)

SENSOR_DESCRIPTIONS: tuple[PajGpsSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: PajGpsConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class PajGpsSensor(PajGpsEntity, SensorEntity):
    entity_description: PajGpsSensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: PajGpsCoordinator, device_id: int, description: PajGpsSensorEntityDescription) -> None: ...
    @property
    @override
    def native_value(self) -> int | None: ...

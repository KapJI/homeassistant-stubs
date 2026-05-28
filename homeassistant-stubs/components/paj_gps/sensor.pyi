from . import PajGpsConfigEntry as PajGpsConfigEntry
from .coordinator import PajGpsCoordinator as PajGpsCoordinator
from .entity import PajGpsEntity as PajGpsEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import UnitOfSpeed as UnitOfSpeed
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pajgps_api.models.trackpoint import TrackPoint as TrackPoint

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class PajGpsSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[TrackPoint], int | None]

SENSOR_DESCRIPTIONS: tuple[PajGpsSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: PajGpsConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class PajGpsSensor(PajGpsEntity, SensorEntity):
    entity_description: PajGpsSensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: PajGpsCoordinator, device_id: int, description: PajGpsSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> int | None: ...

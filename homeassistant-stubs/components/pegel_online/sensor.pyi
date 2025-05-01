from .coordinator import PegelOnlineConfigEntry as PegelOnlineConfigEntry, PegelOnlineDataUpdateCoordinator as PegelOnlineDataUpdateCoordinator
from .entity import PegelOnlineEntity as PegelOnlineEntity
from _typeshed import Incomplete
from aiopegelonline.models import CurrentMeasurement as CurrentMeasurement, StationMeasurements as StationMeasurements
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import ATTR_LATITUDE as ATTR_LATITUDE, ATTR_LONGITUDE as ATTR_LONGITUDE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

@dataclass(frozen=True, kw_only=True)
class PegelOnlineSensorEntityDescription(SensorEntityDescription):
    measurement_fn: Callable[[StationMeasurements], CurrentMeasurement | None]

SENSORS: tuple[PegelOnlineSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: PegelOnlineConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class PegelOnlineSensor(PegelOnlineEntity, SensorEntity):
    entity_description: PegelOnlineSensorEntityDescription
    _attr_unique_id: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    def __init__(self, coordinator: PegelOnlineDataUpdateCoordinator, description: PegelOnlineSensorEntityDescription) -> None: ...
    @property
    def measurement(self) -> CurrentMeasurement: ...
    @property
    def native_value(self) -> float: ...

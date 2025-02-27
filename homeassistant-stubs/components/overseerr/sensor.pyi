from .const import REQUESTS as REQUESTS
from .coordinator import OverseerrConfigEntry as OverseerrConfigEntry, OverseerrCoordinator as OverseerrCoordinator
from .entity import OverseerrEntity as OverseerrEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from python_overseerr import RequestCount as RequestCount

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class OverseerrSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[RequestCount], int]

SENSORS: tuple[OverseerrSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: OverseerrConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class OverseerrSensor(OverseerrEntity, SensorEntity):
    entity_description: OverseerrSensorEntityDescription
    _attr_translation_key: Incomplete
    def __init__(self, coordinator: OverseerrCoordinator, description: OverseerrSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> int: ...

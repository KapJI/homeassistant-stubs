from .coordinator import RDWConfigEntry as RDWConfigEntry, RDWDataUpdateCoordinator as RDWDataUpdateCoordinator
from .entity import RDWEntity as RDWEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from datetime import date
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from vehicle import Vehicle as Vehicle

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class RDWSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[Vehicle], date | str | float | None]

SENSORS: tuple[RDWSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: RDWConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class RDWSensorEntity(RDWEntity, SensorEntity):
    entity_description: RDWSensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: RDWDataUpdateCoordinator, description: RDWSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> date | str | float | None: ...

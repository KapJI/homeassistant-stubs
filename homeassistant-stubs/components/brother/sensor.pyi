from .const import DOMAIN as DOMAIN
from .coordinator import BrotherConfigEntry as BrotherConfigEntry, BrotherDataUpdateCoordinator as BrotherDataUpdateCoordinator
from .entity import BrotherPrinterEntity as BrotherPrinterEntity
from _typeshed import Incomplete
from brother import BrotherSensors as BrotherSensors
from collections.abc import Callable as Callable
from dataclasses import dataclass
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType

PARALLEL_UPDATES: int
ATTR_COUNTER: str
ATTR_REMAINING_PAGES: str
_LOGGER: Incomplete

@dataclass(frozen=True, kw_only=True)
class BrotherSensorEntityDescription(SensorEntityDescription):
    value: Callable[[BrotherSensors], StateType | datetime]

SENSOR_TYPES: tuple[BrotherSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: BrotherConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class BrotherPrinterSensor(BrotherPrinterEntity, SensorEntity):
    entity_description: BrotherSensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: BrotherDataUpdateCoordinator, description: BrotherSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> StateType | datetime: ...

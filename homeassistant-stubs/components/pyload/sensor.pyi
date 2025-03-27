from .const import UNIT_DOWNLOADS as UNIT_DOWNLOADS
from .coordinator import PyLoadConfigEntry as PyLoadConfigEntry, PyLoadData as PyLoadData
from .entity import BasePyLoadEntity as BasePyLoadEntity
from collections.abc import Callable as Callable
from dataclasses import dataclass
from enum import StrEnum
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import UnitOfDataRate as UnitOfDataRate, UnitOfInformation as UnitOfInformation
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType

PARALLEL_UPDATES: int

class PyLoadSensorEntity(StrEnum):
    ACTIVE = 'active'
    FREE_SPACE = 'free_space'
    QUEUE = 'queue'
    SPEED = 'speed'
    TOTAL = 'total'

@dataclass(kw_only=True, frozen=True)
class PyLoadSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[PyLoadData], StateType]

SENSOR_DESCRIPTIONS: tuple[PyLoadSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: PyLoadConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class PyLoadSensor(BasePyLoadEntity, SensorEntity):
    entity_description: PyLoadSensorEntityDescription
    @property
    def native_value(self) -> StateType: ...

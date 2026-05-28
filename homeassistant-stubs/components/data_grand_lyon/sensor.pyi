from .const import SUBENTRY_TYPE_STOP as SUBENTRY_TYPE_STOP, SUBENTRY_TYPE_VELOV_STATION as SUBENTRY_TYPE_VELOV_STATION
from .coordinator import DataGrandLyonConfigEntry as DataGrandLyonConfigEntry
from .entity import DataGrandLyonTclEntity as DataGrandLyonTclEntity, DataGrandLyonVelovEntity as DataGrandLyonVelovEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from data_grand_lyon_ha import TclPassage as TclPassage, VelovStation as VelovStation
from dataclasses import dataclass
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType

PARALLEL_UPDATES: int
_TZ_PARIS: Incomplete
_DEPARTURE_TYPE_OPTIONS: Incomplete

def _departure_time(departure: TclPassage) -> datetime: ...

@dataclass(frozen=True, kw_only=True)
class DataGrandLyonStopSensorEntityDescription(SensorEntityDescription):
    departure_index: int
    value_fn: Callable[[TclPassage], StateType | datetime]

STOP_SENSOR_DESCRIPTIONS: tuple[DataGrandLyonStopSensorEntityDescription, ...]

@dataclass(frozen=True, kw_only=True)
class DataGrandLyonVelovSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[VelovStation], StateType | datetime]

VELOV_SENSOR_DESCRIPTIONS: tuple[DataGrandLyonVelovSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: DataGrandLyonConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class DataGrandLyonStopSensor(DataGrandLyonTclEntity, SensorEntity):
    entity_description: DataGrandLyonStopSensorEntityDescription
    @property
    def available(self) -> bool: ...
    @property
    def native_value(self) -> StateType | datetime: ...

class DataGrandLyonVelovSensor(DataGrandLyonVelovEntity, SensorEntity):
    entity_description: DataGrandLyonVelovSensorEntityDescription
    @property
    def native_value(self) -> StateType | datetime: ...

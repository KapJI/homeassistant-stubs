from .const import SUBENTRY_TYPE_PARK_AND_RIDE as SUBENTRY_TYPE_PARK_AND_RIDE, SUBENTRY_TYPE_STOP as SUBENTRY_TYPE_STOP, SUBENTRY_TYPE_VELOV_STATION as SUBENTRY_TYPE_VELOV_STATION
from .coordinator import DataGrandLyonConfigEntry as DataGrandLyonConfigEntry
from .entity import DataGrandLyonParkAndRideEntity as DataGrandLyonParkAndRideEntity, DataGrandLyonTclEntity as DataGrandLyonTclEntity, DataGrandLyonVelovEntity as DataGrandLyonVelovEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from data_grand_lyon_ha import TclParkAndRide as TclParkAndRide, TclPassage as TclPassage, VelovStation as VelovStation
from dataclasses import dataclass
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from typing import override

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

@dataclass(frozen=True, kw_only=True)
class DataGrandLyonParkAndRideSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[TclParkAndRide], StateType]

PARK_AND_RIDE_SENSOR_DESCRIPTIONS: tuple[DataGrandLyonParkAndRideSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: DataGrandLyonConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class DataGrandLyonStopSensor(DataGrandLyonTclEntity, SensorEntity):
    entity_description: DataGrandLyonStopSensorEntityDescription
    @property
    @override
    def available(self) -> bool: ...
    @property
    @override
    def native_value(self) -> StateType | datetime: ...

class DataGrandLyonVelovSensor(DataGrandLyonVelovEntity, SensorEntity):
    entity_description: DataGrandLyonVelovSensorEntityDescription
    @property
    @override
    def native_value(self) -> StateType | datetime: ...

class DataGrandLyonParkAndRideSensor(DataGrandLyonParkAndRideEntity, SensorEntity):
    entity_description: DataGrandLyonParkAndRideSensorEntityDescription
    @property
    @override
    def native_value(self) -> StateType: ...

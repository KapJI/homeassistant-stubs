from .const import DOMAIN as DOMAIN
from .coordinator import LiebherrConfigEntry as LiebherrConfigEntry, LiebherrCoordinator as LiebherrCoordinator
from .entity import LiebherrZoneEntity as LiebherrZoneEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from pyliebherrhomeapi import TemperatureControl as TemperatureControl

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class LiebherrSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[TemperatureControl], StateType]
    unit_fn: Callable[[TemperatureControl], str]

SENSOR_TYPES: tuple[LiebherrSensorEntityDescription, ...]

def _create_sensor_entities(coordinators: list[LiebherrCoordinator]) -> list[LiebherrSensor]: ...
async def async_setup_entry(hass: HomeAssistant, entry: LiebherrConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class LiebherrSensor(LiebherrZoneEntity, SensorEntity):
    entity_description: LiebherrSensorEntityDescription
    _attr_unique_id: Incomplete
    _attr_name: Incomplete
    _attr_translation_key: Incomplete
    def __init__(self, coordinator: LiebherrCoordinator, zone_id: int, description: LiebherrSensorEntityDescription) -> None: ...
    @property
    def native_unit_of_measurement(self) -> str | None: ...
    @property
    def native_value(self) -> StateType: ...
    @property
    def available(self) -> bool: ...

from . import AirobotConfigEntry as AirobotConfigEntry
from .coordinator import AirobotDataUpdateCoordinator as AirobotDataUpdateCoordinator
from .entity import AirobotEntity as AirobotEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import CONCENTRATION_PARTS_PER_MILLION as CONCENTRATION_PARTS_PER_MILLION, EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, UnitOfTemperature as UnitOfTemperature, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.util.dt import utcnow as utcnow
from homeassistant.util.variance import ignore_variance as ignore_variance
from pyairobotrest.models import ThermostatStatus as ThermostatStatus

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class AirobotSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[ThermostatStatus], StateType | datetime]
    supported_fn: Callable[[ThermostatStatus], bool] = ...

uptime_to_stable_datetime: Incomplete
SENSOR_TYPES: tuple[AirobotSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: AirobotConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class AirobotSensor(AirobotEntity, SensorEntity):
    entity_description: AirobotSensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: AirobotDataUpdateCoordinator, description: AirobotSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> StateType | datetime: ...

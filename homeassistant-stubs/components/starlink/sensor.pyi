from .coordinator import StarlinkConfigEntry as StarlinkConfigEntry, StarlinkData as StarlinkData
from .entity import StarlinkEntity as StarlinkEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from datetime import datetime
from homeassistant.components.sensor import RestoreSensor as RestoreSensor, SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import DEGREE as DEGREE, EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, UnitOfDataRate as UnitOfDataRate, UnitOfEnergy as UnitOfEnergy, UnitOfInformation as UnitOfInformation, UnitOfPower as UnitOfPower, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.util.dt import now as now
from homeassistant.util.variance import ignore_variance as ignore_variance

async def async_setup_entry(hass: HomeAssistant, config_entry: StarlinkConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

@dataclass(frozen=True, kw_only=True)
class StarlinkSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[StarlinkData], datetime | StateType]
    entity_class: Callable

class StarlinkSensorEntity(StarlinkEntity, SensorEntity):
    entity_description: StarlinkSensorEntityDescription
    @property
    def native_value(self) -> StateType | datetime: ...

class StarlinkAccumulationSensor(StarlinkSensorEntity, RestoreSensor):
    _attr_native_value: int | float
    @property
    def native_value(self) -> int | float: ...
    async def async_added_to_hass(self) -> None: ...

uptime_to_stable_datetime: Incomplete
SENSORS: tuple[StarlinkSensorEntityDescription, ...]

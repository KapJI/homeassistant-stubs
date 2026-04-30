from .const import HEART_RATE as HEART_RATE, HRV as HRV, PRESSURE as PRESSURE, RESPIRATORY_RATE as RESPIRATORY_RATE, SLEEP_DURATION as SLEEP_DURATION, SLEEP_NUMBER as SLEEP_NUMBER, SLEEP_SCORE as SLEEP_SCORE
from .coordinator import SleepIQConfigEntry as SleepIQConfigEntry, SleepIQDataUpdateCoordinator as SleepIQDataUpdateCoordinator, SleepIQSleepDataCoordinator as SleepIQSleepDataCoordinator
from .entity import SleepIQSleeperEntity as SleepIQSleeperEntity
from _typeshed import Incomplete
from asyncsleepiq import SleepIQBed as SleepIQBed, SleepIQSleeper as SleepIQSleeper
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

@dataclass(frozen=True, kw_only=True)
class SleepIQSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[SleepIQSleeper], float | int | None]

BED_SENSORS: tuple[SleepIQSensorEntityDescription, ...]
SLEEP_HEALTH_SENSORS: tuple[SleepIQSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: SleepIQConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class SleepIQSensorEntity(SleepIQSleeperEntity[SleepIQDataUpdateCoordinator | SleepIQSleepDataCoordinator], SensorEntity):
    entity_description: SleepIQSensorEntityDescription
    def __init__(self, coordinator: SleepIQDataUpdateCoordinator | SleepIQSleepDataCoordinator, bed: SleepIQBed, sleeper: SleepIQSleeper, description: SleepIQSensorEntityDescription) -> None: ...
    _attr_native_value: Incomplete
    @callback
    def _async_update_attrs(self) -> None: ...

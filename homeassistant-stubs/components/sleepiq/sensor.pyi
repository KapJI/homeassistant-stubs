from .const import DOMAIN as DOMAIN, PRESSURE as PRESSURE, SLEEP_NUMBER as SLEEP_NUMBER
from .coordinator import SleepIQData as SleepIQData
from .entity import SleepIQSleeperEntity as SleepIQSleeperEntity
from asyncsleepiq import SleepIQBed as SleepIQBed, SleepIQSleeper as SleepIQSleeper
from homeassistant.components.sensor import SensorEntity as SensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from typing import Any

SENSORS: Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SleepIQSensorEntity(SleepIQSleeperEntity, SensorEntity):
    _attr_icon: str
    sensor_type: Any
    def __init__(self, coordinator: DataUpdateCoordinator, bed: SleepIQBed, sleeper: SleepIQSleeper, sensor_type: str) -> None: ...
    _attr_native_value: Any
    def _async_update_attrs(self) -> None: ...

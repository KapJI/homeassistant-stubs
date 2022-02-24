from .const import DOMAIN as DOMAIN, SLEEP_NUMBER as SLEEP_NUMBER
from .coordinator import SleepIQData as SleepIQData
from .entity import SleepIQSensor as SleepIQSensor
from asyncsleepiq import SleepIQBed as SleepIQBed, SleepIQSleeper as SleepIQSleeper
from homeassistant.components.sensor import SensorEntity as SensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SleepNumberSensorEntity(SleepIQSensor, SensorEntity):
    _attr_icon: str
    def __init__(self, coordinator: DataUpdateCoordinator, bed: SleepIQBed, sleeper: SleepIQSleeper) -> None: ...
    _attr_native_value: Any
    def _async_update_attrs(self) -> None: ...

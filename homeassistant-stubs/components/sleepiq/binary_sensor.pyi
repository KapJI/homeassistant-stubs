from .const import DOMAIN as DOMAIN, ICON_EMPTY as ICON_EMPTY, ICON_OCCUPIED as ICON_OCCUPIED, IS_IN_BED as IS_IN_BED
from .coordinator import SleepIQData as SleepIQData
from .entity import SleepIQSensor as SleepIQSensor
from asyncsleepiq import SleepIQBed as SleepIQBed, SleepIQSleeper as SleepIQSleeper
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class IsInBedBinarySensor(SleepIQSensor, BinarySensorEntity):
    _attr_device_class: Any
    def __init__(self, coordinator: DataUpdateCoordinator, bed: SleepIQBed, sleeper: SleepIQSleeper) -> None: ...
    _attr_is_on: Any
    _attr_icon: Any
    def _async_update_attrs(self) -> None: ...

from .const import STATUSES_ON as STATUSES_ON
from .coordinator import UptimeRobotConfigEntry as UptimeRobotConfigEntry
from .entity import UptimeRobotEntity as UptimeRobotEntity
from .utils import new_device_listener as new_device_listener
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pyuptimerobot import UptimeRobotMonitor as UptimeRobotMonitor
from typing import override

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: UptimeRobotConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class UptimeRobotBinarySensor(UptimeRobotEntity, BinarySensorEntity):
    @property
    @override
    def is_on(self) -> bool: ...

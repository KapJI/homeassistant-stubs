from . import UptimeRobotDataUpdateCoordinator as UptimeRobotDataUpdateCoordinator
from .const import DOMAIN as DOMAIN
from .entity import UptimeRobotEntity as UptimeRobotEntity
from homeassistant.components.sensor import SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any, TypedDict

class StatusValue(TypedDict):
    value: str
    icon: str

SENSORS_INFO: Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class UptimeRobotSensor(UptimeRobotEntity, SensorEntity):
    @property
    def native_value(self) -> str: ...
    @property
    def icon(self) -> str: ...

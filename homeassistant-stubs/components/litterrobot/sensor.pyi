from .const import DOMAIN as DOMAIN
from .entity import LitterRobotEntity as LitterRobotEntity
from .hub import LitterRobotHub as LitterRobotHub
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import PERCENTAGE as PERCENTAGE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pylitterbot.robot import Robot as Robot
from typing import Any

def icon_for_gauge_level(gauge_level: Union[int, None] = ..., offset: int = ...) -> str: ...

class LitterRobotSensorEntityDescription(SensorEntityDescription):
    icon_fn: Callable[[Any], Union[str, None]]
    should_report: Callable[[Robot], bool]
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, unit_of_measurement, last_reset, native_unit_of_measurement, state_class, icon_fn, should_report) -> None: ...

class LitterRobotSensorEntity(LitterRobotEntity, SensorEntity):
    entity_description: LitterRobotSensorEntityDescription
    def __init__(self, robot: Robot, hub: LitterRobotHub, description: LitterRobotSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> Union[float, datetime, str, None]: ...
    @property
    def icon(self) -> Union[str, None]: ...

ROBOT_SENSORS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

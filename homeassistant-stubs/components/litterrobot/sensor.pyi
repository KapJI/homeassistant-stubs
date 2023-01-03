from .const import DOMAIN as DOMAIN
from .entity import LitterRobotEntity as LitterRobotEntity, _RobotT as _RobotT, async_update_unique_id as async_update_unique_id
from .hub import LitterRobotHub as LitterRobotHub
from collections.abc import Callable as Callable
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import MASS_POUNDS as MASS_POUNDS, PERCENTAGE as PERCENTAGE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pylitterbot import Robot as Robot
from typing import Any

def icon_for_gauge_level(gauge_level: Union[int, None] = ..., offset: int = ...) -> str: ...

class RobotSensorEntityDescription(SensorEntityDescription):
    icon_fn: Callable[[Any], Union[str, None]]
    should_report: Callable[[_RobotT], bool]
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, unit_of_measurement, suggested_unit_of_measurement, last_reset, native_unit_of_measurement, state_class, icon_fn, should_report) -> None: ...

class LitterRobotSensorEntity(LitterRobotEntity[_RobotT], SensorEntity):
    entity_description: RobotSensorEntityDescription[_RobotT]
    @property
    def native_value(self) -> Union[float, datetime, str, None]: ...
    @property
    def icon(self) -> Union[str, None]: ...

ROBOT_SENSOR_MAP: dict[type[Robot], list[RobotSensorEntityDescription]]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

from . import LitterRobotConfigEntry as LitterRobotConfigEntry
from .entity import LitterRobotEntity as LitterRobotEntity, _RobotT as _RobotT
from collections.abc import Callable as Callable
from dataclasses import dataclass
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, UnitOfMass as UnitOfMass
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pylitterbot import Robot as Robot
from typing import Any, Generic

def icon_for_gauge_level(gauge_level: int | None = None, offset: int = 0) -> str: ...

@dataclass(frozen=True)
class RobotSensorEntityDescription(SensorEntityDescription, Generic[_RobotT]):
    icon_fn: Callable[[Any], str | None] = ...
    should_report: Callable[[_RobotT], bool] = ...
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=..., last_reset=..., native_unit_of_measurement=..., options=..., state_class=..., suggested_display_precision=..., suggested_unit_of_measurement=..., icon_fn=..., should_report=...) -> None: ...

class LitterRobotSensorEntity(LitterRobotEntity[_RobotT], SensorEntity):
    entity_description: RobotSensorEntityDescription[_RobotT]
    @property
    def native_value(self) -> float | datetime | str | None: ...
    @property
    def icon(self) -> str | None: ...

ROBOT_SENSOR_MAP: dict[type[Robot], list[RobotSensorEntityDescription]]

async def async_setup_entry(hass: HomeAssistant, entry: LitterRobotConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

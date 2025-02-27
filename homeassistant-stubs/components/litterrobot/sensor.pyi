from .coordinator import LitterRobotConfigEntry as LitterRobotConfigEntry
from .entity import LitterRobotEntity as LitterRobotEntity, _WhiskerEntityT as _WhiskerEntityT
from collections.abc import Callable as Callable
from dataclasses import dataclass
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, UnitOfMass as UnitOfMass
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pylitterbot import Robot as Robot
from typing import Any, Generic

def icon_for_gauge_level(gauge_level: int | None = None, offset: int = 0) -> str: ...

@dataclass(frozen=True, kw_only=True)
class RobotSensorEntityDescription(SensorEntityDescription, Generic[_WhiskerEntityT]):
    icon_fn: Callable[[Any], str | None] = ...
    value_fn: Callable[[_WhiskerEntityT], float | datetime | str | None]

ROBOT_SENSOR_MAP: dict[type[Robot], list[RobotSensorEntityDescription]]
PET_SENSORS: list[RobotSensorEntityDescription]

async def async_setup_entry(hass: HomeAssistant, entry: LitterRobotConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class LitterRobotSensorEntity(LitterRobotEntity[_WhiskerEntityT], SensorEntity):
    entity_description: RobotSensorEntityDescription[_WhiskerEntityT]
    @property
    def native_value(self) -> float | datetime | str | None: ...
    @property
    def icon(self) -> str | None: ...

from .coordinator import LitterRobotConfigEntry as LitterRobotConfigEntry
from .entity import LitterRobotEntity as LitterRobotEntity, _WhiskerEntityT as _WhiskerEntityT
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pylitterbot import Robot
from typing import Generic

@dataclass(frozen=True, kw_only=True)
class RobotBinarySensorEntityDescription(BinarySensorEntityDescription, Generic[_WhiskerEntityT]):
    is_on_fn: Callable[[_WhiskerEntityT], bool]

BINARY_SENSOR_MAP: dict[type[Robot], tuple[RobotBinarySensorEntityDescription, ...]]

async def async_setup_entry(hass: HomeAssistant, entry: LitterRobotConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class LitterRobotBinarySensorEntity(LitterRobotEntity[_WhiskerEntityT], BinarySensorEntity):
    entity_description: RobotBinarySensorEntityDescription[_WhiskerEntityT]
    @property
    def is_on(self) -> bool: ...

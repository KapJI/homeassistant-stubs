from .const import DOMAIN as DOMAIN
from .coordinator import LitterRobotDataUpdateCoordinator as LitterRobotDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from pylitterbot import Robot
from typing import Generic, TypeVar

_RobotT = TypeVar('_RobotT', bound=Robot)

class LitterRobotEntity(CoordinatorEntity[LitterRobotDataUpdateCoordinator], Generic[_RobotT]):
    _attr_has_entity_name: bool
    robot: Incomplete
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, robot: _RobotT, coordinator: LitterRobotDataUpdateCoordinator, description: EntityDescription) -> None: ...
    async def async_added_to_hass(self) -> None: ...

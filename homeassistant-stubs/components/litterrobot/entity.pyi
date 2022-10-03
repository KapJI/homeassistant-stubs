from .const import DOMAIN as DOMAIN
from .hub import LitterRobotHub as LitterRobotHub
from _typeshed import Incomplete
from collections.abc import Iterable
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo, EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator
from pylitterbot import Robot
from typing import TypeVar

_RobotT = TypeVar('_RobotT', bound=Robot)

class LitterRobotEntity(CoordinatorEntity[DataUpdateCoordinator[bool]]):
    _attr_has_entity_name: bool
    robot: Incomplete
    hub: Incomplete
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    _attr_name: Incomplete
    def __init__(self, robot: _RobotT, hub: LitterRobotHub, description: EntityDescription) -> None: ...
    @property
    def device_info(self) -> DeviceInfo: ...
    async def async_added_to_hass(self) -> None: ...

def async_update_unique_id(hass: HomeAssistant, domain: str, entities: Iterable[LitterRobotEntity[_RobotT]]) -> None: ...

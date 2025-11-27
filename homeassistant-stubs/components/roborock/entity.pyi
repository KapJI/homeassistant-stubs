from .const import DOMAIN as DOMAIN
from .coordinator import RoborockDataUpdateCoordinator as RoborockDataUpdateCoordinator, RoborockDataUpdateCoordinatorA01 as RoborockDataUpdateCoordinatorA01
from _typeshed import Incomplete
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from roborock.data import Status as Status
from roborock.devices.traits.v1.command import CommandTrait as CommandTrait
from roborock.roborock_typing import RoborockCommand
from typing import Any

class RoborockEntity(Entity):
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, unique_id: str, device_info: DeviceInfo) -> None: ...

class RoborockEntityV1(RoborockEntity):
    _api: Incomplete
    def __init__(self, unique_id: str, device_info: DeviceInfo, api: CommandTrait) -> None: ...
    async def send(self, command: RoborockCommand | str, params: dict[str, Any] | list[Any] | int | None = None) -> dict: ...

class RoborockCoordinatedEntityV1(RoborockEntityV1, CoordinatorEntity[RoborockDataUpdateCoordinator]):
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    def __init__(self, unique_id: str, coordinator: RoborockDataUpdateCoordinator, is_dock_entity: bool = False) -> None: ...
    @property
    def _device_status(self) -> Status: ...
    async def send(self, command: RoborockCommand | str, params: dict[str, Any] | list[Any] | int | None = None) -> dict: ...

class RoborockCoordinatedEntityA01(RoborockEntity, CoordinatorEntity[RoborockDataUpdateCoordinatorA01]):
    _attr_unique_id: Incomplete
    def __init__(self, unique_id: str, coordinator: RoborockDataUpdateCoordinatorA01) -> None: ...

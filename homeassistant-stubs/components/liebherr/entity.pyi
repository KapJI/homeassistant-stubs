from .const import DOMAIN as DOMAIN, MANUFACTURER as MANUFACTURER
from .coordinator import LiebherrCoordinator as LiebherrCoordinator
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from pyliebherrhomeapi import DeviceControl as DeviceControl, TemperatureControl as TemperatureControl
from typing import Any

ZONE_POSITION_MAP: Incomplete

class LiebherrEntity(CoordinatorEntity[LiebherrCoordinator]):
    _attr_has_entity_name: bool
    _attr_device_info: Incomplete
    def __init__(self, coordinator: LiebherrCoordinator) -> None: ...
    async def _async_send_command[ControlT: DeviceControl](self, command: Coroutine[Any, Any, None], control: ControlT | None = None, updater: Callable[[ControlT], ControlT] | None = None) -> None: ...

class LiebherrZoneEntity(LiebherrEntity):
    _zone_id: Incomplete
    def __init__(self, coordinator: LiebherrCoordinator, zone_id: int) -> None: ...
    @property
    def temperature_control(self) -> TemperatureControl | None: ...
    def _get_zone_translation_key(self) -> str | None: ...

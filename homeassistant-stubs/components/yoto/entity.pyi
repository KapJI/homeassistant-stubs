from .const import DOMAIN as DOMAIN, MANUFACTURER as MANUFACTURER
from .coordinator import YotoDataUpdateCoordinator as YotoDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC, DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any, override
from yoto_api import YotoPlayer as YotoPlayer

class YotoEntity(CoordinatorEntity[YotoDataUpdateCoordinator]):
    _attr_has_entity_name: bool
    _player_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: YotoDataUpdateCoordinator, player: YotoPlayer) -> None: ...
    @property
    def player(self) -> YotoPlayer: ...
    @property
    @override
    def available(self) -> bool: ...

class YotoPlayerEntity(YotoEntity):
    @property
    @override
    def available(self) -> bool: ...

class YotoConfigEntity(YotoEntity):
    async def _async_set_config(self, **fields: Any) -> None: ...

from .const import DOMAIN as DOMAIN
from .coordinator import CasperGlowCoordinator as CasperGlowCoordinator
from _typeshed import Incomplete
from collections.abc import Awaitable
from homeassistant.components.bluetooth.passive_update_coordinator import PassiveBluetoothCoordinatorEntity as PassiveBluetoothCoordinatorEntity
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo, format_mac as format_mac

class CasperGlowEntity(PassiveBluetoothCoordinatorEntity[CasperGlowCoordinator]):
    _attr_has_entity_name: bool
    _device: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: CasperGlowCoordinator) -> None: ...
    async def _async_command(self, coro: Awaitable[None]) -> None: ...

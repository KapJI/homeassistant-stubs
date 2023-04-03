from .const import DOMAIN as DOMAIN
from .hub import Device as Device, MikrotikDataUpdateCoordinator as MikrotikDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.components.device_tracker import ScannerEntity as ScannerEntity, SourceType as SourceType
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
def update_items(coordinator: MikrotikDataUpdateCoordinator, async_add_entities: AddEntitiesCallback, tracked: dict[str, MikrotikDataUpdateCoordinatorTracker]) -> None: ...

class MikrotikDataUpdateCoordinatorTracker(CoordinatorEntity[MikrotikDataUpdateCoordinator], ScannerEntity):
    device: Incomplete
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, device: Device, coordinator: MikrotikDataUpdateCoordinator) -> None: ...
    @property
    def is_connected(self) -> bool: ...
    @property
    def source_type(self) -> SourceType: ...
    @property
    def hostname(self) -> str: ...
    @property
    def mac_address(self) -> str: ...
    @property
    def ip_address(self) -> str | None: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any] | None: ...

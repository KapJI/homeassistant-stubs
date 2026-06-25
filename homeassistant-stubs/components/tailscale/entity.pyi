from .const import DOMAIN as DOMAIN
from .coordinator import TailscaleDataUpdateCoordinator as TailscaleDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from tailscale import Device as TailscaleDevice
from typing import override

class TailscaleEntity(CoordinatorEntity[TailscaleDataUpdateCoordinator]):
    _attr_has_entity_name: bool
    entity_description: Incomplete
    device_id: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, *, coordinator: TailscaleDataUpdateCoordinator, device: TailscaleDevice, description: EntityDescription) -> None: ...
    @property
    @override
    def device_info(self) -> DeviceInfo: ...

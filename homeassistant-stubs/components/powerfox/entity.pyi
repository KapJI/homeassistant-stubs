from .const import DOMAIN as DOMAIN
from .coordinator import PowerfoxBaseCoordinator as PowerfoxBaseCoordinator
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from powerfox import Device as Device
from typing import Any

class PowerfoxEntity[CoordinatorT: PowerfoxBaseCoordinator[Any]](CoordinatorEntity[CoordinatorT]):
    _attr_has_entity_name: bool
    _attr_device_info: Incomplete
    def __init__(self, coordinator: CoordinatorT, device: Device) -> None: ...

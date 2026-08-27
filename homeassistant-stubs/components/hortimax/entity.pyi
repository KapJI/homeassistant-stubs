from .const import DOMAIN as DOMAIN, MANUFACTURER as MANUFACTURER
from .coordinator import HortimaxCoordinator as HortimaxCoordinator, source_key as source_key
from _typeshed import Incomplete
from aiohortos import Readout as Readout
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import override

class HortimaxEntity(CoordinatorEntity[HortimaxCoordinator]):
    _attr_has_entity_name: bool
    _device_id: Incomplete
    _key: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: HortimaxCoordinator, device_id: str, key: str) -> None: ...
    @property
    @override
    def available(self) -> bool: ...
    @property
    def readout(self) -> Readout | None: ...

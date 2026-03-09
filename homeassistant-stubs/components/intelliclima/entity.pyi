from .const import DOMAIN as DOMAIN
from .coordinator import IntelliClimaCoordinator as IntelliClimaCoordinator
from _typeshed import Incomplete
from homeassistant.const import ATTR_CONNECTIONS as ATTR_CONNECTIONS, ATTR_MODEL as ATTR_MODEL, ATTR_SW_VERSION as ATTR_SW_VERSION
from homeassistant.helpers.device_registry import CONNECTION_BLUETOOTH as CONNECTION_BLUETOOTH, CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC, DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from pyintelliclima.intelliclima_types import IntelliClimaC800 as IntelliClimaC800, IntelliClimaECO as IntelliClimaECO

class IntelliClimaEntity(CoordinatorEntity[IntelliClimaCoordinator]):
    _attr_has_entity_name: bool
    _attr_device_info: Incomplete
    _device_id: Incomplete
    _device_sn: Incomplete
    def __init__(self, coordinator: IntelliClimaCoordinator, device: IntelliClimaECO | IntelliClimaC800) -> None: ...

class IntelliClimaECOEntity(IntelliClimaEntity):
    _attr_device_info: DeviceInfo
    def __init__(self, coordinator: IntelliClimaCoordinator, device: IntelliClimaECO) -> None: ...
    @property
    def _device_data(self) -> IntelliClimaECO: ...
    @property
    def available(self) -> bool: ...

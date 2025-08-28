from .const import DOMAIN as DOMAIN
from .coordinator import AladdinConnectCoordinator as AladdinConnectCoordinator
from _typeshed import Incomplete
from genie_partner_sdk.client import AladdinConnectClient as AladdinConnectClient
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class AladdinConnectEntity(CoordinatorEntity[AladdinConnectCoordinator]):
    _attr_has_entity_name: bool
    _attr_device_info: Incomplete
    _device_id: Incomplete
    _number: Incomplete
    def __init__(self, coordinator: AladdinConnectCoordinator) -> None: ...
    @property
    def client(self) -> AladdinConnectClient: ...

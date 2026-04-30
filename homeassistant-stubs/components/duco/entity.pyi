from .const import DOMAIN as DOMAIN
from .coordinator import DucoCoordinator as DucoCoordinator
from _typeshed import Incomplete
from duco.models import Node as Node
from homeassistant.const import ATTR_VIA_DEVICE as ATTR_VIA_DEVICE
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC, DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class DucoEntity(CoordinatorEntity[DucoCoordinator]):
    _attr_has_entity_name: bool
    _node_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: DucoCoordinator, node: Node) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def _node(self) -> Node: ...

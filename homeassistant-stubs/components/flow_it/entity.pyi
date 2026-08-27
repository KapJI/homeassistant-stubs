from .const import DOMAIN as DOMAIN
from .coordinator import FlowItCoordinator as FlowItCoordinator
from _typeshed import Incomplete
from flow_it_api.client import FlowItVMCMachine as FlowItVMCMachine
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class FlowItVmcEntity(CoordinatorEntity[FlowItCoordinator]):
    _attr_has_entity_name: bool
    entity_description: Incomplete
    vmc: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: FlowItCoordinator, vmc: FlowItVMCMachine, entity_description: EntityDescription) -> None: ...

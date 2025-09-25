from .const import DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN
from .coordinator import PortainerCoordinator as PortainerCoordinator, PortainerCoordinatorData as PortainerCoordinatorData
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from pyportainer.models.docker import DockerContainer as DockerContainer

class PortainerCoordinatorEntity(CoordinatorEntity[PortainerCoordinator]):
    _attr_has_entity_name: bool

class PortainerEndpointEntity(PortainerCoordinatorEntity):
    _device_info: Incomplete
    device_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, device_info: PortainerCoordinatorData, coordinator: PortainerCoordinator) -> None: ...

class PortainerContainerEntity(PortainerCoordinatorEntity):
    _device_info: Incomplete
    device_id: Incomplete
    endpoint_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, device_info: DockerContainer, coordinator: PortainerCoordinator, via_device: PortainerCoordinatorData) -> None: ...

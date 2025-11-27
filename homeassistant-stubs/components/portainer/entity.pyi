from .const import DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN
from .coordinator import PortainerContainerData as PortainerContainerData, PortainerCoordinator as PortainerCoordinator, PortainerCoordinatorData as PortainerCoordinatorData
from _typeshed import Incomplete
from homeassistant.const import CONF_URL as CONF_URL
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

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
    device_name: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, device_info: PortainerContainerData, coordinator: PortainerCoordinator, via_device: PortainerCoordinatorData) -> None: ...
    @property
    def container_data(self) -> PortainerContainerData: ...

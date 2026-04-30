from .const import DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN
from .coordinator import DockerVolume as DockerVolume, PortainerContainerData as PortainerContainerData, PortainerCoordinator as PortainerCoordinator, PortainerCoordinatorData as PortainerCoordinatorData, PortainerStackData as PortainerStackData, PortainerVolumeData as PortainerVolumeData
from _typeshed import Incomplete
from homeassistant.const import CONF_URL as CONF_URL
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class PortainerCoordinatorEntity(CoordinatorEntity[PortainerCoordinator]):
    _attr_has_entity_name: bool

class PortainerEndpointEntity(PortainerCoordinatorEntity):
    entity_description: Incomplete
    _device_info: Incomplete
    device_id: Incomplete
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: PortainerCoordinator, entity_description: EntityDescription, device_info: PortainerCoordinatorData) -> None: ...
    @property
    def available(self) -> bool: ...

class PortainerContainerEntity(PortainerCoordinatorEntity):
    entity_description: Incomplete
    _device_info: Incomplete
    device_id: Incomplete
    endpoint_id: Incomplete
    device_name: Incomplete
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: PortainerCoordinator, entity_description: EntityDescription, device_info: PortainerContainerData, via_device: PortainerCoordinatorData) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def container_data(self) -> PortainerContainerData: ...

class PortainerStackEntity(PortainerCoordinatorEntity):
    entity_description: Incomplete
    _device_info: Incomplete
    stack_id: Incomplete
    device_name: Incomplete
    endpoint_id: Incomplete
    endpoint_name: Incomplete
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: PortainerCoordinator, entity_description: EntityDescription, device_info: PortainerStackData, via_device: PortainerCoordinatorData) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def stack_data(self) -> PortainerStackData: ...

class PortainerVolumeEntity(PortainerCoordinatorEntity):
    entity_description: Incomplete
    _device_info: Incomplete
    volume_name: Incomplete
    endpoint_id: Incomplete
    endpoint_name: Incomplete
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: PortainerCoordinator, entity_description: EntityDescription, device_info: DockerVolume, via_device: PortainerCoordinatorData) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def volume_data(self) -> PortainerVolumeData: ...

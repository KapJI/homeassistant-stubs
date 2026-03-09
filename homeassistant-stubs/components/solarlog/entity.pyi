from .const import DOMAIN as DOMAIN
from .coordinator import SolarLogBasicDataCoordinator as SolarLogBasicDataCoordinator, SolarLogDeviceDataCoordinator as SolarLogDeviceDataCoordinator, SolarLogLongtimeDataCoordinator as SolarLogLongtimeDataCoordinator
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorEntityDescription as SensorEntityDescription
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from homeassistant.util import slugify as slugify

class SolarLogBasicCoordinatorEntity(CoordinatorEntity[SolarLogBasicDataCoordinator]):
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    entity_description: Incomplete
    def __init__(self, coordinator: SolarLogBasicDataCoordinator, description: SensorEntityDescription) -> None: ...

class SolarLogInverterEntity(CoordinatorEntity[SolarLogDeviceDataCoordinator]):
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    device_id: Incomplete
    entity_description: Incomplete
    def __init__(self, coordinator: SolarLogDeviceDataCoordinator, description: SensorEntityDescription, device_id: int) -> None: ...

class SolarLogLongtimeCoordinatorEntity(CoordinatorEntity[SolarLogLongtimeDataCoordinator]):
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    entity_description: Incomplete
    def __init__(self, coordinator: SolarLogLongtimeDataCoordinator, description: SensorEntityDescription) -> None: ...

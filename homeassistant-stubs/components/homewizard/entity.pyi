from .const import DOMAIN as DOMAIN
from .coordinator import HWEnergyDeviceUpdateCoordinator as HWEnergyDeviceUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.const import ATTR_IDENTIFIERS as ATTR_IDENTIFIERS
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class HomeWizardEntity(CoordinatorEntity[HWEnergyDeviceUpdateCoordinator]):
    _attr_has_entity_name: bool
    _attr_device_info: Incomplete
    def __init__(self, coordinator: HWEnergyDeviceUpdateCoordinator) -> None: ...

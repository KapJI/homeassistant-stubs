from .const import DOMAIN as DOMAIN
from .coordinator import BatteryData as BatteryData, ZinvoltDeviceCoordinator as ZinvoltDeviceCoordinator
from _typeshed import Incomplete
from homeassistant.const import ATTR_VIA_DEVICE as ATTR_VIA_DEVICE
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from zinvolt.models import Unit as Unit

class ZinvoltEntity(CoordinatorEntity[ZinvoltDeviceCoordinator]):
    _attr_has_entity_name: bool
    _attr_device_info: Incomplete
    def __init__(self, coordinator: ZinvoltDeviceCoordinator) -> None: ...

class ZinvoltUnitEntity(ZinvoltEntity):
    unit_serial_number: Incomplete
    serial_number: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: ZinvoltDeviceCoordinator, unit_serial_number: str) -> None: ...
    @property
    def battery(self) -> BatteryData: ...
    @property
    def battery_unit(self) -> Unit: ...
    @property
    def available(self) -> bool: ...

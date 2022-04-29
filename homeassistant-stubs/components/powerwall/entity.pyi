from .const import DOMAIN as DOMAIN, MANUFACTURER as MANUFACTURER, MODEL as MODEL, POWERWALL_BASE_INFO as POWERWALL_BASE_INFO, POWERWALL_COORDINATOR as POWERWALL_COORDINATOR
from .models import PowerwallData as PowerwallData, PowerwallRuntimeData as PowerwallRuntimeData
from _typeshed import Incomplete
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator

class PowerWallEntity(CoordinatorEntity[DataUpdateCoordinator[PowerwallData]]):
    base_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, powerwall_data: PowerwallRuntimeData) -> None: ...
    @property
    def data(self) -> PowerwallData: ...

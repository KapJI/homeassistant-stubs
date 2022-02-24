from .const import DOMAIN as DOMAIN, MANUFACTURER as MANUFACTURER, MODEL as MODEL, POWERWALL_BASE_INFO as POWERWALL_BASE_INFO, POWERWALL_COORDINATOR as POWERWALL_COORDINATOR
from .models import PowerwallData as PowerwallData, PowerwallRuntimeData as PowerwallRuntimeData
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

class PowerWallEntity(CoordinatorEntity[PowerwallData]):
    base_unique_id: Any
    _attr_device_info: Any
    def __init__(self, powerwall_data: PowerwallRuntimeData) -> None: ...
    @property
    def data(self) -> PowerwallData: ...

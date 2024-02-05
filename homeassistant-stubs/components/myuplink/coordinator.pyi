from _typeshed import Incomplete
from dataclasses import dataclass
from datetime import datetime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from myuplink.api import MyUplinkAPI as MyUplinkAPI
from myuplink.models import Device as Device, DevicePoint as DevicePoint, System as System

_LOGGER: Incomplete

@dataclass
class CoordinatorData:
    systems: list[System]
    devices: dict[str, Device]
    points: dict[str, dict[str, DevicePoint]]
    time: datetime
    def __init__(self, systems, devices, points, time) -> None: ...

class MyUplinkDataCoordinator(DataUpdateCoordinator[CoordinatorData]):
    api: Incomplete
    def __init__(self, hass: HomeAssistant, api: MyUplinkAPI) -> None: ...
    async def _async_update_data(self) -> CoordinatorData: ...

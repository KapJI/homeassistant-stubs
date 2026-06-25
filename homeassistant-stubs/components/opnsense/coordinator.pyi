from .const import SCAN_INTERVAL as SCAN_INTERVAL
from .types import DeviceDetails as DeviceDetails, DeviceDetailsByMAC as DeviceDetailsByMAC, OPNsenseConfigEntry as OPNsenseConfigEntry
from _typeshed import Incomplete
from aiopnsense import OPNsenseClient as OPNsenseClient
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryError as ConfigEntryError
from homeassistant.helpers.device_registry import format_mac as format_mac
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import override

_LOGGER: Incomplete

class OPNsenseDeviceTrackerCoordinator(DataUpdateCoordinator[DeviceDetailsByMAC]):
    client: Incomplete
    interfaces: Incomplete
    tracked_devices: set[str]
    def __init__(self, hass: HomeAssistant, config_entry: OPNsenseConfigEntry, client: OPNsenseClient, interfaces: list[str]) -> None: ...
    def _get_mac_addrs(self, devices: list[DeviceDetails]) -> DeviceDetailsByMAC: ...
    @override
    async def _async_update_data(self) -> DeviceDetailsByMAC: ...

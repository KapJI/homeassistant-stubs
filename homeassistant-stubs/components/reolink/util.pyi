from .const import DOMAIN as DOMAIN
from .host import ReolinkHost as ReolinkHost
from dataclasses import dataclass
from homeassistant import config_entries as config_entries
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import device_registry as dr
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator

type ReolinkConfigEntry = config_entries.ConfigEntry[ReolinkData]
@dataclass
class ReolinkData:
    host: ReolinkHost
    device_coordinator: DataUpdateCoordinator[None]
    firmware_coordinator: DataUpdateCoordinator[None]
    def __init__(self, host, device_coordinator, firmware_coordinator) -> None: ...

def is_connected(hass: HomeAssistant, config_entry: config_entries.ConfigEntry) -> bool: ...
def get_device_uid_and_ch(device: dr.DeviceEntry, host: ReolinkHost) -> tuple[list[str], int | None, bool]: ...

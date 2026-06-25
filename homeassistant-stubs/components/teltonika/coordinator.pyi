from . import TeltonikaConfigEntry as TeltonikaConfigEntry
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC, DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from teltasync import Teltasync as Teltasync
from teltasync.modems import ModemStatusFull
from typing import override

_LOGGER: Incomplete
SCAN_INTERVAL: Incomplete
AUTH_ERROR_CODES: Incomplete

class TeltonikaDataUpdateCoordinator(DataUpdateCoordinator[dict[str, ModemStatusFull]]):
    device_info: DeviceInfo
    client: Incomplete
    base_url: Incomplete
    def __init__(self, hass: HomeAssistant, client: Teltasync, config_entry: TeltonikaConfigEntry, base_url: str) -> None: ...
    @override
    async def _async_setup(self) -> None: ...
    @override
    async def _async_update_data(self) -> dict[str, ModemStatusFull]: ...

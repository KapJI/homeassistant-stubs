from .const import DOMAIN as DOMAIN
from bimmer_connected.account import ConnectedDriveAccount
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import Any

SCAN_INTERVAL: Any
_LOGGER: Any

class BMWDataUpdateCoordinator(DataUpdateCoordinator):
    account: ConnectedDriveAccount
    _username: Any
    _password: Any
    _region: Any
    read_only: Any
    def __init__(self, hass: HomeAssistant, *, username: str, password: str, region: str, read_only: bool = ...) -> None: ...
    async def _async_update_data(self) -> None: ...
    def notify_listeners(self) -> None: ...

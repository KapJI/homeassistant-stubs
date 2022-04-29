from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from bimmer_connected.account import ConnectedDriveAccount
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

SCAN_INTERVAL: Incomplete
_LOGGER: Incomplete

class BMWDataUpdateCoordinator(DataUpdateCoordinator):
    account: ConnectedDriveAccount
    _username: Incomplete
    _password: Incomplete
    _region: Incomplete
    read_only: Incomplete
    def __init__(self, hass: HomeAssistant, *, username: str, password: str, region: str, read_only: bool = ...) -> None: ...
    async def _async_update_data(self) -> None: ...
    def notify_listeners(self) -> None: ...

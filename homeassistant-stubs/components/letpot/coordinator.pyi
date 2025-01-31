from . import LetPotConfigEntry as LetPotConfigEntry
from .const import REQUEST_UPDATE_TIMEOUT as REQUEST_UPDATE_TIMEOUT
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from letpot.deviceclient import LetPotDeviceClient
from letpot.models import AuthenticationInfo as AuthenticationInfo, LetPotDevice as LetPotDevice, LetPotDeviceStatus

_LOGGER: Incomplete

class LetPotDeviceCoordinator(DataUpdateCoordinator[LetPotDeviceStatus]):
    config_entry: LetPotConfigEntry
    device: LetPotDevice
    device_client: LetPotDeviceClient
    _info: Incomplete
    def __init__(self, hass: HomeAssistant, info: AuthenticationInfo, device: LetPotDevice) -> None: ...
    def _handle_status_update(self, status: LetPotDeviceStatus) -> None: ...
    async def _async_setup(self) -> None: ...
    async def _async_update_data(self) -> LetPotDeviceStatus: ...

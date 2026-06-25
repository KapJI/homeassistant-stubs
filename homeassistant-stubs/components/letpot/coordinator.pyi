from .const import REQUEST_UPDATE_TIMEOUT as REQUEST_UPDATE_TIMEOUT
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from letpot.deviceclient import LetPotDeviceClient as LetPotDeviceClient
from letpot.models import LetPotDevice as LetPotDevice, LetPotDeviceStatus, LetPotGardenStatus
from typing import override

_LOGGER: Incomplete
type LetPotConfigEntry = ConfigEntry[list[LetPotDeviceCoordinator[LetPotGardenStatus]]]

class LetPotDeviceCoordinator[_DataT: LetPotDeviceStatus](DataUpdateCoordinator[_DataT]):
    config_entry: LetPotConfigEntry
    device: LetPotDevice
    device_client: LetPotDeviceClient
    def __init__(self, hass: HomeAssistant, config_entry: LetPotConfigEntry, device: LetPotDevice, device_client: LetPotDeviceClient) -> None: ...
    def _handle_status_update(self, status: _DataT) -> None: ...
    @override
    async def _async_setup(self) -> None: ...
    @override
    async def _async_update_data(self) -> _DataT: ...

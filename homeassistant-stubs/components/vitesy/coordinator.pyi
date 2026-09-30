from .const import DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from aiovitesy.api import VitesyDevice, VitesyModeStatus as VitesyModeStatus
from collections.abc import Iterator
from contextlib import contextmanager
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_EMAIL as CONF_EMAIL, CONF_PASSWORD as CONF_PASSWORD
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import override

type VitesyConfigEntry = ConfigEntry[VitesyDataUpdateCoordinator]
UPDATE_INTERVAL: Incomplete

def supports_mode(device: VitesyDevice) -> bool: ...
@contextmanager
def _translate_errors(*, auth_recoverable: bool = False) -> Iterator[None]: ...

class VitesyDataUpdateCoordinator(DataUpdateCoordinator[dict[str, VitesyDevice]]):
    config_entry: VitesyConfigEntry
    api: Incomplete
    mode_status: dict[str, VitesyModeStatus]
    def __init__(self, hass: HomeAssistant, config_entry: VitesyConfigEntry) -> None: ...
    @override
    async def _async_setup(self) -> None: ...
    @override
    async def _async_update_data(self) -> dict[str, VitesyDevice]: ...
    async def _async_get_mode_status(self, devices: dict[str, VitesyDevice]) -> dict[str, VitesyModeStatus]: ...

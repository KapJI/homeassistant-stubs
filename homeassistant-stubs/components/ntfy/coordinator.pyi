from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from aiontfy import Account as NtfyAccount, Ntfy as Ntfy
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

_LOGGER: Incomplete
type NtfyConfigEntry = ConfigEntry[NtfyDataUpdateCoordinator]

class NtfyDataUpdateCoordinator(DataUpdateCoordinator[NtfyAccount]):
    config_entry: NtfyConfigEntry
    ntfy: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: NtfyConfigEntry, ntfy: Ntfy) -> None: ...
    async def _async_update_data(self) -> NtfyAccount: ...

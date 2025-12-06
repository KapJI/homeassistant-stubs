from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from datetime import timedelta
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from pyrituals import Account as Account, Diffuser as Diffuser

_LOGGER: Incomplete

class RitualsDataUpdateCoordinator(DataUpdateCoordinator[None]):
    config_entry: ConfigEntry
    account: Incomplete
    diffuser: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: ConfigEntry, account: Account, diffuser: Diffuser, update_interval: timedelta) -> None: ...
    async def _async_update_data(self) -> None: ...

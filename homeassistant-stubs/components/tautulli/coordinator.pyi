from .const import DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from pytautulli import PyTautulli as PyTautulli, PyTautulliApiActivity as PyTautulliApiActivity, PyTautulliApiHomeStats as PyTautulliApiHomeStats, PyTautulliApiUser as PyTautulliApiUser
from pytautulli.models.host_configuration import PyTautulliHostConfiguration as PyTautulliHostConfiguration

class TautulliDataUpdateCoordinator(DataUpdateCoordinator):
    config_entry: ConfigEntry
    host_configuration: Incomplete
    api_client: Incomplete
    activity: Incomplete
    home_stats: Incomplete
    users: Incomplete
    def __init__(self, hass: HomeAssistant, host_configuration: PyTautulliHostConfiguration, api_client: PyTautulli) -> None: ...
    async def _async_update_data(self) -> None: ...

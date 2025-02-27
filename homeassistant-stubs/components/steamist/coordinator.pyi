from _typeshed import Incomplete
from aiosteamist import Steamist as Steamist, SteamistStatus
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_NAME as CONF_NAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator

_LOGGER: Incomplete

class SteamistDataUpdateCoordinator(DataUpdateCoordinator[SteamistStatus]):
    config_entry: ConfigEntry
    client: Incomplete
    device_name: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: ConfigEntry, client: Steamist) -> None: ...
    async def _async_update_data(self) -> SteamistStatus: ...

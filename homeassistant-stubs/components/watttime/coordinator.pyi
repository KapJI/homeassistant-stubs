from .const import DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from aiowatttime import Client as Client
from aiowatttime.emissions import RealTimeEmissionsResponseType
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_LATITUDE as CONF_LATITUDE, CONF_LONGITUDE as CONF_LONGITUDE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

DEFAULT_UPDATE_INTERVAL: Incomplete

class WattTimeCoordinator(DataUpdateCoordinator[RealTimeEmissionsResponseType]):
    config_entry: ConfigEntry
    client: Incomplete
    def __init__(self, hass: HomeAssistant, entry: ConfigEntry, client: Client) -> None: ...
    async def _async_update_data(self) -> RealTimeEmissionsResponseType: ...

from .const import DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_API_KEY as CONF_API_KEY
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from trmnl.models import Device

type TRMNLConfigEntry = ConfigEntry[TRMNLCoordinator]
class TRMNLCoordinator(DataUpdateCoordinator[dict[int, Device]]):
    config_entry: TRMNLConfigEntry
    client: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: TRMNLConfigEntry) -> None: ...
    async def _async_update_data(self) -> dict[int, Device]: ...

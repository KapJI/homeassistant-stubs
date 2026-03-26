from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from aioimmich.server.models import ImmichServerAbout as ImmichServerAbout, ImmichServerStatistics as ImmichServerStatistics, ImmichServerStorage as ImmichServerStorage, ImmichServerVersionCheck as ImmichServerVersionCheck
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_HOST as CONF_HOST, CONF_PORT as CONF_PORT, CONF_SSL as CONF_SSL, CONF_VERIFY_SSL as CONF_VERIFY_SSL
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

_LOGGER: Incomplete

@dataclass
class ImmichData:
    server_about: ImmichServerAbout
    server_storage: ImmichServerStorage
    server_usage: ImmichServerStatistics | None
    server_version_check: ImmichServerVersionCheck | None
type ImmichConfigEntry = ConfigEntry[ImmichDataUpdateCoordinator]

class ImmichDataUpdateCoordinator(DataUpdateCoordinator[ImmichData]):
    config_entry: ImmichConfigEntry
    api: Incomplete
    is_admin: bool
    configuration_url: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: ImmichConfigEntry) -> None: ...
    async def _async_setup(self) -> None: ...
    async def _async_update_data(self) -> ImmichData: ...

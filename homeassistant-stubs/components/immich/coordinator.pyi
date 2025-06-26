from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from aioimmich import Immich as Immich
from aioimmich.server.models import ImmichServerAbout as ImmichServerAbout, ImmichServerStatistics as ImmichServerStatistics, ImmichServerStorage as ImmichServerStorage, ImmichServerVersionCheck as ImmichServerVersionCheck
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PORT as CONF_PORT, CONF_SSL as CONF_SSL
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
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
    is_admin: Incomplete
    configuration_url: Incomplete
    def __init__(self, hass: HomeAssistant, entry: ConfigEntry, api: Immich, is_admin: bool) -> None: ...
    async def _async_update_data(self) -> ImmichData: ...

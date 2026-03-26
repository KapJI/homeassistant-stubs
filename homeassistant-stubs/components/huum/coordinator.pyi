from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from huum.schemas import HuumStatusResponse

type HuumConfigEntry = ConfigEntry[HuumDataUpdateCoordinator]
_LOGGER: Incomplete
UPDATE_INTERVAL: Incomplete

class HuumDataUpdateCoordinator(DataUpdateCoordinator[HuumStatusResponse]):
    config_entry: HuumConfigEntry
    huum: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: HuumConfigEntry) -> None: ...
    async def _async_update_data(self) -> HuumStatusResponse: ...

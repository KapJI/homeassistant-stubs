from .const import DOMAIN as DOMAIN
from .models import AirobotData as AirobotData
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

_LOGGER: Incomplete
UPDATE_INTERVAL: Incomplete
type AirobotConfigEntry = ConfigEntry[AirobotDataUpdateCoordinator]

class AirobotDataUpdateCoordinator(DataUpdateCoordinator[AirobotData]):
    config_entry: AirobotConfigEntry
    client: Incomplete
    def __init__(self, hass: HomeAssistant, entry: AirobotConfigEntry) -> None: ...
    async def _async_update_data(self) -> AirobotData: ...

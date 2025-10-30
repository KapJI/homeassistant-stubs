from .const import CONF_STATION_NUMBER as CONF_STATION_NUMBER, LOGGER as LOGGER
from _typeshed import Incomplete
from aiowaqi import WAQIAirQuality, WAQIClient as WAQIClient
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigSubentry as ConfigSubentry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

type WAQIConfigEntry = ConfigEntry[dict[str, WAQIDataUpdateCoordinator]]
class WAQIDataUpdateCoordinator(DataUpdateCoordinator[WAQIAirQuality]):
    config_entry: WAQIConfigEntry
    _client: Incomplete
    subentry: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: WAQIConfigEntry, subentry: ConfigSubentry, client: WAQIClient) -> None: ...
    async def _async_update_data(self) -> WAQIAirQuality: ...

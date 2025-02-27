from .const import DEFAULT_SCAN_INTERVAL as DEFAULT_SCAN_INTERVAL, DOMAIN as DOMAIN, LOGGER as LOGGER, TIMEOUT as TIMEOUT
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_LATITUDE as CONF_LATITUDE, CONF_LOCATION as CONF_LOCATION, CONF_LONGITUDE as CONF_LONGITUDE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import aiohttp_client as aiohttp_client
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from pysmhi import SMHIForecast as SMHIForecast

type SMHIConfigEntry = ConfigEntry[SMHIDataUpdateCoordinator]
@dataclass
class SMHIForecastData:
    daily: list[SMHIForecast]
    hourly: list[SMHIForecast]

class SMHIDataUpdateCoordinator(DataUpdateCoordinator[SMHIForecastData]):
    config_entry: SMHIConfigEntry
    _smhi_api: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: SMHIConfigEntry) -> None: ...
    async def _async_update_data(self) -> SMHIForecastData: ...

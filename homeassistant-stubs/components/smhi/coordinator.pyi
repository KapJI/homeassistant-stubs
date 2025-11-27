from .const import DEFAULT_SCAN_INTERVAL as DEFAULT_SCAN_INTERVAL, DOMAIN as DOMAIN, LOGGER as LOGGER, TIMEOUT as TIMEOUT
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_LATITUDE as CONF_LATITUDE, CONF_LOCATION as CONF_LOCATION, CONF_LONGITUDE as CONF_LONGITUDE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import aiohttp_client as aiohttp_client
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from pysmhi import SMHIFireForecast as SMHIFireForecast, SMHIForecast as SMHIForecast

type SMHIConfigEntry = ConfigEntry[tuple[SMHIDataUpdateCoordinator, SMHIFireDataUpdateCoordinator]]
@dataclass
class SMHIForecastData:
    daily: list[SMHIForecast]
    hourly: list[SMHIForecast]
    twice_daily: list[SMHIForecast]

@dataclass
class SMHIFireForecastData:
    fire_daily: list[SMHIFireForecast]
    fire_hourly: list[SMHIFireForecast]

class SMHIDataUpdateCoordinator(DataUpdateCoordinator[SMHIForecastData]):
    config_entry: SMHIConfigEntry
    _smhi_api: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: SMHIConfigEntry) -> None: ...
    async def _async_update_data(self) -> SMHIForecastData: ...
    @property
    def current(self) -> SMHIForecast: ...

class SMHIFireDataUpdateCoordinator(DataUpdateCoordinator[SMHIFireForecastData]):
    config_entry: SMHIConfigEntry
    _smhi_fire_api: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: SMHIConfigEntry) -> None: ...
    async def _async_update_data(self) -> SMHIFireForecastData: ...
    @property
    def fire_current(self) -> SMHIFireForecast: ...

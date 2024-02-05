from .const import DOMAIN as DOMAIN, LOGGER as LOGGER, SCAN_INTERVAL as SCAN_INTERVAL, SERVICE_PHASES as SERVICE_PHASES, SERVICE_SETTINGS as SERVICE_SETTINGS, SERVICE_SMARTMETER as SERVICE_SMARTMETER, SERVICE_WATERMETER as SERVICE_WATERMETER
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from p1monitor import Phases, Settings, SmartMeter, WaterMeter
from typing import TypedDict

PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class P1MonitorData(TypedDict):
    smartmeter: SmartMeter
    phases: Phases
    settings: Settings
    watermeter: WaterMeter | None

class P1MonitorDataUpdateCoordinator(DataUpdateCoordinator[P1MonitorData]):
    config_entry: ConfigEntry
    has_water_meter: bool | None
    p1monitor: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    async def _async_update_data(self) -> P1MonitorData: ...

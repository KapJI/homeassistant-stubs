from .const import CONF_HUB as CONF_HUB, DOMAIN as DOMAIN, LOGGER as LOGGER, OVERKIZ_DEVICE_TO_PLATFORM as OVERKIZ_DEVICE_TO_PLATFORM, PLATFORMS as PLATFORMS, UPDATE_INTERVAL as UPDATE_INTERVAL, UPDATE_INTERVAL_ALL_ASSUMED_STATE as UPDATE_INTERVAL_ALL_ASSUMED_STATE
from .coordinator import OverkizDataUpdateCoordinator as OverkizDataUpdateCoordinator
from collections import defaultdict
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_create_clientsession as async_create_clientsession
from pyoverkiz.models import Device as Device, Scenario as Scenario

class HomeAssistantOverkizData:
    coordinator: OverkizDataUpdateCoordinator
    platforms: defaultdict[Platform, list[Device]]
    scenarios: list[Scenario]
    def __init__(self, coordinator, platforms, scenarios) -> None: ...

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

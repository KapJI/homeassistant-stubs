from . import config_flow as config_flow
from .api import SENZConfigEntryAuth as SENZConfigEntryAuth
from .const import DOMAIN as DOMAIN
from aiosenz import Thermostat
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_CLIENT_ID as CONF_CLIENT_ID, CONF_CLIENT_SECRET as CONF_CLIENT_SECRET, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers import config_entry_oauth2_flow as config_entry_oauth2_flow, httpx_client as httpx_client
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import Any

UPDATE_INTERVAL: Any
_LOGGER: Any
CONFIG_SCHEMA: Any
PLATFORMS: Any
SENZDataUpdateCoordinator = DataUpdateCoordinator[dict[str, Thermostat]]

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

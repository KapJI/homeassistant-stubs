from .const import DOMAIN as DOMAIN
from .coordinator import LunatoneConfigEntry as LunatoneConfigEntry, LunatoneData as LunatoneData, LunatoneDevicesDataUpdateCoordinator as LunatoneDevicesDataUpdateCoordinator, LunatoneInfoDataUpdateCoordinator as LunatoneInfoDataUpdateCoordinator
from homeassistant.const import CONF_URL as CONF_URL, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryError as ConfigEntryError
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from typing import Final

PLATFORMS: Final[list[Platform]]

async def async_setup_entry(hass: HomeAssistant, entry: LunatoneConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: LunatoneConfigEntry) -> bool: ...

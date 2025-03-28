from .coordinator import BraviaTVConfigEntry as BraviaTVConfigEntry, BraviaTVCoordinator as BraviaTVCoordinator
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_MAC as CONF_MAC, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_create_clientsession as async_create_clientsession
from typing import Final

PLATFORMS: Final[list[Platform]]

async def async_setup_entry(hass: HomeAssistant, config_entry: BraviaTVConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, config_entry: BraviaTVConfigEntry) -> bool: ...
async def update_listener(hass: HomeAssistant, config_entry: BraviaTVConfigEntry) -> None: ...

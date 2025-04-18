from .coordinator import KnockiConfigEntry as KnockiConfigEntry, KnockiCoordinator as KnockiCoordinator
from homeassistant.const import CONF_TOKEN as CONF_TOKEN, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from knocki import Event as Event

PLATFORMS: list[Platform]

async def async_setup_entry(hass: HomeAssistant, entry: KnockiConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: KnockiConfigEntry) -> bool: ...

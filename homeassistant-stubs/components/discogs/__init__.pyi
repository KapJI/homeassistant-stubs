import discogs_client
from .const import PLATFORMS as PLATFORMS
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_TOKEN as CONF_TOKEN
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import SERVER_SOFTWARE as SERVER_SOFTWARE

type DiscogsConfigEntry = ConfigEntry[discogs_client.Client]
async def async_setup_entry(hass: HomeAssistant, entry: DiscogsConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: DiscogsConfigEntry) -> bool: ...

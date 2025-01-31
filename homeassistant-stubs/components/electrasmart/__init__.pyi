from .const import CONF_IMEI as CONF_IMEI
from electrasmart.api import ElectraAPI
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_TOKEN as CONF_TOKEN, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession

PLATFORMS: list[Platform]
type ElectraSmartConfigEntry = ConfigEntry[ElectraAPI]

async def async_setup_entry(hass: HomeAssistant, entry: ElectraSmartConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ElectraSmartConfigEntry) -> bool: ...
async def update_listener(hass: HomeAssistant, config_entry: ElectraSmartConfigEntry) -> None: ...

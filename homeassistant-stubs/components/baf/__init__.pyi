from .const import DOMAIN as DOMAIN, QUERY_INTERVAL as QUERY_INTERVAL, RUN_TIMEOUT as RUN_TIMEOUT
from .models import BAFData as BAFData
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_IP_ADDRESS as CONF_IP_ADDRESS, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady

PLATFORMS: list[Platform]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

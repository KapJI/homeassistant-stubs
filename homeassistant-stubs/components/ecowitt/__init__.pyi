from .const import DOMAIN as DOMAIN
from aiohttp import web as web
from homeassistant.components import webhook as webhook
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_WEBHOOK_ID as CONF_WEBHOOK_ID, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, Platform as Platform
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback

PLATFORMS: list[Platform]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

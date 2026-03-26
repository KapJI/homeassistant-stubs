from .const import DISPATCH_CONFIG_UPDATED as DISPATCH_CONFIG_UPDATED, DOMAIN as DOMAIN
from .coordinator import KrakenData as KrakenData
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_SCAN_INTERVAL as CONF_SCAN_INTERVAL, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send

PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool: ...
async def async_options_updated(hass: HomeAssistant, config_entry: ConfigEntry) -> None: ...

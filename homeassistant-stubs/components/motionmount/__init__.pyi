import motionmount
from .const import DOMAIN as DOMAIN, EMPTY_MAC as EMPTY_MAC
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PIN as CONF_PIN, CONF_PORT as CONF_PORT, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.device_registry import format_mac as format_mac

type MotionMountConfigEntry = ConfigEntry[motionmount.MotionMount]
PLATFORMS: list[Platform]

async def async_setup_entry(hass: HomeAssistant, entry: MotionMountConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: MotionMountConfigEntry) -> bool: ...

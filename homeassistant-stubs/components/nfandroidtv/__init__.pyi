from .const import DATA_HASS_CONFIG as DATA_HASS_CONFIG, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_NAME as CONF_NAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers import discovery as discovery
from homeassistant.helpers.typing import ConfigType as ConfigType
from notifications_android_tv.notifications import Notifications

_LOGGER: Incomplete
PLATFORMS: Incomplete
CONFIG_SCHEMA: Incomplete
type NFAndroidTVConfigEntry = ConfigEntry[Notifications]

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: NFAndroidTVConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: NFAndroidTVConfigEntry) -> bool: ...

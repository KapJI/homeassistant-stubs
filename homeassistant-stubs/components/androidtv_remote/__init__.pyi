from .helpers import AndroidTVRemoteConfigEntry as AndroidTVRemoteConfigEntry, create_api as create_api, get_enable_ime as get_enable_ime
from _typeshed import Incomplete
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_NAME as CONF_NAME, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, Platform as Platform
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady

_LOGGER: Incomplete
PLATFORMS: list[Platform]

async def async_setup_entry(hass: HomeAssistant, entry: AndroidTVRemoteConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: AndroidTVRemoteConfigEntry) -> bool: ...

from .const import ATTR_CONFIG_ENTRY_ID as ATTR_CONFIG_ENTRY_ID, DATA_HASS_CONFIG as DATA_HASS_CONFIG, DOMAIN as DOMAIN, PLATFORMS as PLATFORMS, WEBOSTV_EXCEPTIONS as WEBOSTV_EXCEPTIONS
from .helpers import WebOsTvConfigEntry as WebOsTvConfigEntry, update_client_key as update_client_key
from _typeshed import Incomplete
from homeassistant.const import CONF_CLIENT_SECRET as CONF_CLIENT_SECRET, CONF_HOST as CONF_HOST, CONF_NAME as CONF_NAME, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, Platform as Platform
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers import discovery as discovery
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.typing import ConfigType as ConfigType

CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: WebOsTvConfigEntry) -> bool: ...
async def async_update_options(hass: HomeAssistant, entry: WebOsTvConfigEntry) -> None: ...
async def async_unload_entry(hass: HomeAssistant, entry: WebOsTvConfigEntry) -> bool: ...

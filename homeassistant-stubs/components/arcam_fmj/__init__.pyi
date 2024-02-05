from .const import DEFAULT_SCAN_INTERVAL as DEFAULT_SCAN_INTERVAL, DOMAIN as DOMAIN, DOMAIN_DATA_ENTRIES as DOMAIN_DATA_ENTRIES, SIGNAL_CLIENT_DATA as SIGNAL_CLIENT_DATA, SIGNAL_CLIENT_STARTED as SIGNAL_CLIENT_STARTED, SIGNAL_CLIENT_STOPPED as SIGNAL_CLIENT_STOPPED
from _typeshed import Incomplete
from arcam.fmj.client import Client
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PORT as CONF_PORT, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.typing import ConfigType as ConfigType

_LOGGER: Incomplete
CONFIG_SCHEMA: Incomplete
PLATFORMS: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def _run_client(hass: HomeAssistant, client: Client, interval: float) -> None: ...

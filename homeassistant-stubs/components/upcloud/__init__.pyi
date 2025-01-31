from .const import CONFIG_ENTRY_UPDATE_SIGNAL_TEMPLATE as CONFIG_ENTRY_UPDATE_SIGNAL_TEMPLATE, DEFAULT_SCAN_INTERVAL as DEFAULT_SCAN_INTERVAL
from .coordinator import UpCloudConfigEntry as UpCloudConfigEntry, UpCloudDataUpdateCoordinator as UpCloudDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_SCAN_INTERVAL as CONF_SCAN_INTERVAL, CONF_USERNAME as CONF_USERNAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect, async_dispatcher_send as async_dispatcher_send

_LOGGER: Incomplete
PLATFORMS: Incomplete

def _config_entry_update_signal_name(config_entry: UpCloudConfigEntry) -> str: ...
async def _async_signal_options_update(hass: HomeAssistant, config_entry: UpCloudConfigEntry) -> None: ...
async def async_setup_entry(hass: HomeAssistant, entry: UpCloudConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: UpCloudConfigEntry) -> bool: ...

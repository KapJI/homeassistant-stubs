from .const import CONF_IGNORE_STRING as CONF_IGNORE_STRING, CONF_NETWORK as CONF_NETWORK, CONF_SENSOR_STRING as CONF_SENSOR_STRING, CONF_TLS_VER as CONF_TLS_VER, DEFAULT_IGNORE_STRING as DEFAULT_IGNORE_STRING, DEFAULT_SENSOR_STRING as DEFAULT_SENSOR_STRING, DOMAIN as DOMAIN, ISY_CONF_FIRMWARE as ISY_CONF_FIRMWARE, ISY_CONF_MODEL as ISY_CONF_MODEL, ISY_CONF_NAME as ISY_CONF_NAME, MANUFACTURER as MANUFACTURER, PLATFORMS as PLATFORMS, SCHEME_HTTP as SCHEME_HTTP, SCHEME_HTTPS as SCHEME_HTTPS, _LOGGER as _LOGGER
from .helpers import _categorize_nodes as _categorize_nodes, _categorize_programs as _categorize_programs
from .models import IsyConfigEntry as IsyConfigEntry, IsyData as IsyData
from .services import async_setup_services as async_setup_services
from .util import _async_cleanup_registry_entries as _async_cleanup_registry_entries
from _typeshed import Incomplete
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME, CONF_VARIABLES as CONF_VARIABLES, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, Platform as Platform
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers import aiohttp_client as aiohttp_client, device_registry as dr
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.typing import ConfigType as ConfigType
from pyisy import ISY

CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: IsyConfigEntry) -> bool: ...
@callback
def _async_get_or_create_isy_device_in_registry(hass: HomeAssistant, entry: IsyConfigEntry, isy: ISY) -> None: ...
def _create_service_device_info(isy: ISY, name: str, unique_id: str) -> DeviceInfo: ...
async def async_unload_entry(hass: HomeAssistant, entry: IsyConfigEntry) -> bool: ...
async def async_remove_config_entry_device(hass: HomeAssistant, config_entry: IsyConfigEntry, device_entry: dr.DeviceEntry) -> bool: ...

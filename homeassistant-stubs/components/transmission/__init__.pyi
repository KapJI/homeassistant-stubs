import transmission_rpc
from .const import DEFAULT_PATH as DEFAULT_PATH, DEFAULT_SSL as DEFAULT_SSL, DOMAIN as DOMAIN
from .coordinator import TransmissionConfigEntry as TransmissionConfigEntry, TransmissionDataUpdateCoordinator as TransmissionDataUpdateCoordinator
from .errors import AuthenticationError as AuthenticationError, CannotConnect as CannotConnect, UnknownError as UnknownError
from .services import async_setup_services as async_setup_services
from _typeshed import Incomplete
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_NAME as CONF_NAME, CONF_PASSWORD as CONF_PASSWORD, CONF_PATH as CONF_PATH, CONF_PORT as CONF_PORT, CONF_SSL as CONF_SSL, CONF_USERNAME as CONF_USERNAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any

_LOGGER: Incomplete
PLATFORMS: Incomplete
MIGRATION_NAME_TO_KEY: Incomplete
CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: TransmissionConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, config_entry: TransmissionConfigEntry) -> bool: ...
async def async_migrate_entry(hass: HomeAssistant, config_entry: TransmissionConfigEntry) -> bool: ...
async def get_api(hass: HomeAssistant, entry: dict[str, Any]) -> transmission_rpc.Client: ...

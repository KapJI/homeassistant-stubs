from .const import CONF_INSTALLER_CODE as CONF_INSTALLER_CODE, CONF_USER_CODE as CONF_USER_CODE, DOMAIN as DOMAIN
from .services import setup_services as setup_services
from .types import BoschAlarmConfigEntry as BoschAlarmConfigEntry
from _typeshed import Incomplete
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_MAC as CONF_MAC, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC
from homeassistant.helpers.typing import ConfigType as ConfigType

CONFIG_SCHEMA: Incomplete
PLATFORMS: list[Platform]

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: BoschAlarmConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: BoschAlarmConfigEntry) -> bool: ...

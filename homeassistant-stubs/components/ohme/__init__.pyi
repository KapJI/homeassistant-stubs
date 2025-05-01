from .const import DOMAIN as DOMAIN, PLATFORMS as PLATFORMS
from .coordinator import OhmeAdvancedSettingsCoordinator as OhmeAdvancedSettingsCoordinator, OhmeChargeSessionCoordinator as OhmeChargeSessionCoordinator, OhmeConfigEntry as OhmeConfigEntry, OhmeDeviceInfoCoordinator as OhmeDeviceInfoCoordinator, OhmeRuntimeData as OhmeRuntimeData
from .services import async_setup_services as async_setup_services
from _typeshed import Incomplete
from homeassistant.const import CONF_EMAIL as CONF_EMAIL, CONF_PASSWORD as CONF_PASSWORD
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.typing import ConfigType as ConfigType

CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: OhmeConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: OhmeConfigEntry) -> bool: ...

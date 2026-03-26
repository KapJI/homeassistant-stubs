from .const import API_MAX_RETRIES as API_MAX_RETRIES, DOMAIN as DOMAIN
from .coordinator import PortainerCoordinator as PortainerCoordinator
from .services import async_setup_services as async_setup_services
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_API_TOKEN as CONF_API_TOKEN, CONF_HOST as CONF_HOST, CONF_URL as CONF_URL, CONF_VERIFY_SSL as CONF_VERIFY_SSL, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_create_clientsession as async_create_clientsession
from homeassistant.helpers.device_registry import DeviceEntry as DeviceEntry
from homeassistant.helpers.typing import ConfigType as ConfigType

_PLATFORMS: list[Platform]
CONFIG_SCHEMA: Incomplete
type PortainerConfigEntry = ConfigEntry[PortainerCoordinator]
_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: PortainerConfigEntry) -> bool: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: PortainerConfigEntry) -> bool: ...
async def async_migrate_entry(hass: HomeAssistant, entry: PortainerConfigEntry) -> bool: ...
async def async_remove_config_entry_device(hass: HomeAssistant, entry: PortainerConfigEntry, device: DeviceEntry) -> bool: ...

from .const import CONF_USE_BLUETOOTH as CONF_USE_BLUETOOTH, DOMAIN as DOMAIN
from .coordinator import LaMarzoccoConfigEntry as LaMarzoccoConfigEntry, LaMarzoccoConfigUpdateCoordinator as LaMarzoccoConfigUpdateCoordinator, LaMarzoccoRuntimeData as LaMarzoccoRuntimeData, LaMarzoccoScheduleUpdateCoordinator as LaMarzoccoScheduleUpdateCoordinator, LaMarzoccoSettingsUpdateCoordinator as LaMarzoccoSettingsUpdateCoordinator, LaMarzoccoStatisticsUpdateCoordinator as LaMarzoccoStatisticsUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.components.bluetooth import async_discovered_service_info as async_discovered_service_info
from homeassistant.const import CONF_MAC as CONF_MAC, CONF_PASSWORD as CONF_PASSWORD, CONF_TOKEN as CONF_TOKEN, CONF_USERNAME as CONF_USERNAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession

PLATFORMS: Incomplete
BT_MODEL_PREFIXES: Incomplete
_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: LaMarzoccoConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: LaMarzoccoConfigEntry) -> bool: ...
async def async_migrate_entry(hass: HomeAssistant, entry: LaMarzoccoConfigEntry) -> bool: ...

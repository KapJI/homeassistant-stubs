from .const import DOMAIN as DOMAIN
from .coordinator import DuckDnsConfigEntry as DuckDnsConfigEntry, DuckDnsUpdateCoordinator as DuckDnsUpdateCoordinator
from .services import async_setup_services as async_setup_services
from _typeshed import Incomplete
from homeassistant.config_entries import SOURCE_IMPORT as SOURCE_IMPORT
from homeassistant.const import CONF_ACCESS_TOKEN as CONF_ACCESS_TOKEN, CONF_DOMAIN as CONF_DOMAIN
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.typing import ConfigType as ConfigType

_LOGGER: Incomplete
CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: DuckDnsConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: DuckDnsConfigEntry) -> bool: ...

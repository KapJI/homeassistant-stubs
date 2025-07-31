from .const import DOMAIN as DOMAIN
from .coordinator import ImmichConfigEntry as ImmichConfigEntry, ImmichDataUpdateCoordinator as ImmichDataUpdateCoordinator
from .services import async_setup_services as async_setup_services
from _typeshed import Incomplete
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_HOST as CONF_HOST, CONF_PORT as CONF_PORT, CONF_SSL as CONF_SSL, CONF_VERIFY_SSL as CONF_VERIFY_SSL, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.typing import ConfigType as ConfigType

CONFIG_SCHEMA: Incomplete
PLATFORMS: list[Platform]

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ImmichConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ImmichConfigEntry) -> bool: ...

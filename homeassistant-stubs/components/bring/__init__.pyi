from .const import DOMAIN as DOMAIN
from .coordinator import BringActivityCoordinator as BringActivityCoordinator, BringConfigEntry as BringConfigEntry, BringCoordinators as BringCoordinators, BringDataUpdateCoordinator as BringDataUpdateCoordinator
from .services import async_setup_services as async_setup_services
from _typeshed import Incomplete
from homeassistant.const import CONF_EMAIL as CONF_EMAIL, CONF_PASSWORD as CONF_PASSWORD, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.typing import ConfigType as ConfigType

CONFIG_SCHEMA: Incomplete
PLATFORMS: list[Platform]
_LOGGER: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: BringConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: BringConfigEntry) -> bool: ...

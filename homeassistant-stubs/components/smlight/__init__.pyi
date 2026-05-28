from .const import DOMAIN as DOMAIN
from .coordinator import SmConfigEntry as SmConfigEntry, SmDataUpdateCoordinator as SmDataUpdateCoordinator, SmFirmwareUpdateCoordinator as SmFirmwareUpdateCoordinator, SmlightData as SmlightData
from .services import async_setup_services as async_setup_services
from _typeshed import Incomplete
from homeassistant.const import CONF_HOST as CONF_HOST, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.typing import ConfigType as ConfigType

CONFIG_SCHEMA: Incomplete
PLATFORMS: list[Platform]

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: SmConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: SmConfigEntry) -> bool: ...

from .const import DOMAIN as DOMAIN, MANUFACTURER as MANUFACTURER
from .coordinator import AirzoneConfigEntry as AirzoneConfigEntry, AirzoneUpdateCoordinator as AirzoneUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_ID as CONF_ID, CONF_PORT as CONF_PORT, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import aiohttp_client as aiohttp_client

PLATFORMS: list[Platform]
_LOGGER: Incomplete

async def _async_migrate_unique_ids(hass: HomeAssistant, entry: AirzoneConfigEntry, coordinator: AirzoneUpdateCoordinator) -> None: ...
async def async_setup_entry(hass: HomeAssistant, entry: AirzoneConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: AirzoneConfigEntry) -> bool: ...
async def async_migrate_entry(hass: HomeAssistant, entry: AirzoneConfigEntry) -> bool: ...

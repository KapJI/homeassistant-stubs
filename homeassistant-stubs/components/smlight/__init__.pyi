from .coordinator import SmConfigEntry as SmConfigEntry, SmDataUpdateCoordinator as SmDataUpdateCoordinator, SmFirmwareUpdateCoordinator as SmFirmwareUpdateCoordinator, SmlightData as SmlightData
from homeassistant.const import CONF_HOST as CONF_HOST, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from pysmlight import Info as Info, Radio as Radio

PLATFORMS: list[Platform]

async def async_setup_entry(hass: HomeAssistant, entry: SmConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: SmConfigEntry) -> bool: ...
def get_radio(info: Info, idx: int) -> Radio: ...

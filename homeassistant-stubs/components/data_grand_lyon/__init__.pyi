from .coordinator import DataGrandLyonConfigEntry as DataGrandLyonConfigEntry, DataGrandLyonData as DataGrandLyonData, DataGrandLyonTclCoordinator as DataGrandLyonTclCoordinator, DataGrandLyonVelovCoordinator as DataGrandLyonVelovCoordinator
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator

PLATFORMS: list[Platform]

async def async_setup_entry(hass: HomeAssistant, entry: DataGrandLyonConfigEntry) -> bool: ...
async def async_update_entry(hass: HomeAssistant, entry: DataGrandLyonConfigEntry) -> None: ...
async def async_unload_entry(hass: HomeAssistant, entry: DataGrandLyonConfigEntry) -> bool: ...

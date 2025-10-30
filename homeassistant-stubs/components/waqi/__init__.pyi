from .const import CONF_STATION_NUMBER as CONF_STATION_NUMBER, DOMAIN as DOMAIN, SUBENTRY_TYPE_STATION as SUBENTRY_TYPE_STATION
from .coordinator import WAQIConfigEntry as WAQIConfigEntry, WAQIDataUpdateCoordinator as WAQIDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigSubentry as ConfigSubentry
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.typing import ConfigType as ConfigType

CONFIG_SCHEMA: Incomplete
PLATFORMS: list[Platform]

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: WAQIConfigEntry) -> bool: ...
async def async_update_entry(hass: HomeAssistant, entry: WAQIConfigEntry) -> None: ...
async def async_unload_entry(hass: HomeAssistant, entry: WAQIConfigEntry) -> bool: ...
async def async_migrate_integration(hass: HomeAssistant) -> None: ...

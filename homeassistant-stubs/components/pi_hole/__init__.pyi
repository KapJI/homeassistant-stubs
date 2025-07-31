from .const import CONF_STATISTICS_ONLY as CONF_STATISTICS_ONLY, DOMAIN as DOMAIN, MIN_TIME_BETWEEN_UPDATES as MIN_TIME_BETWEEN_UPDATES, VERSION_6_RESPONSE_TO_5_ERROR as VERSION_6_RESPONSE_TO_5_ERROR
from _typeshed import Incomplete
from dataclasses import dataclass
from hole import Hole, HoleV5 as HoleV5, HoleV6 as HoleV6
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_HOST as CONF_HOST, CONF_LOCATION as CONF_LOCATION, CONF_NAME as CONF_NAME, CONF_SSL as CONF_SSL, CONF_VERIFY_SSL as CONF_VERIFY_SSL, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import Any, Literal

_LOGGER: Incomplete
PLATFORMS: Incomplete
type PiHoleConfigEntry = ConfigEntry[PiHoleData]

@dataclass
class PiHoleData:
    api: Hole
    coordinator: DataUpdateCoordinator[None]
    api_version: int

async def async_setup_entry(hass: HomeAssistant, entry: PiHoleConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
def api_by_version(hass: HomeAssistant, entry: dict[str, Any], version: int, password: str | None = None) -> HoleV5 | HoleV6: ...
async def determine_api_version(hass: HomeAssistant, entry: dict[str, Any]) -> Literal[5, 6]: ...

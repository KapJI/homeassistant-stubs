from .const import DOMAIN as DOMAIN
from .coordinator import GlancesDataUpdateCoordinator as GlancesDataUpdateCoordinator
from _typeshed import Incomplete
from glances_api import Glances
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_NAME as CONF_NAME, CONF_VERIFY_SSL as CONF_VERIFY_SSL, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.httpx_client import get_async_client as get_async_client
from typing import Any

PLATFORMS: Incomplete
CONFIG_SCHEMA: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
def get_api(hass: HomeAssistant, entry_data: dict[str, Any]) -> Glances: ...

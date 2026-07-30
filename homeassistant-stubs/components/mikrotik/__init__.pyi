from .const import ATTR_MANUFACTURER as ATTR_MANUFACTURER, DOMAIN as DOMAIN
from .coordinator import MikrotikConfigEntry as MikrotikConfigEntry, MikrotikDataUpdateCoordinator as MikrotikDataUpdateCoordinator, get_api as get_api, mikrotik_config_entry_errors as mikrotik_config_entry_errors
from _typeshed import Incomplete
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from librouteros import Api as Api
from typing import Any

PLATFORMS: Incomplete

def _call_api(data: dict[str, Any]) -> Api: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: MikrotikConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, config_entry: MikrotikConfigEntry) -> bool: ...

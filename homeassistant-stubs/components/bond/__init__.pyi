from .const import BPUP_STOP as BPUP_STOP, BPUP_SUBS as BPUP_SUBS, BRIDGE_MAKE as BRIDGE_MAKE, DOMAIN as DOMAIN, HUB as HUB
from .utils import BondHub as BondHub
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_ACCESS_TOKEN as CONF_ACCESS_TOKEN, CONF_HOST as CONF_HOST
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers import device_registry as dr
from homeassistant.helpers.entity import SLOW_UPDATE_WARNING as SLOW_UPDATE_WARNING
from typing import Any

PLATFORMS: Any
_API_TIMEOUT: Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
def _async_remove_old_device_identifiers(config_entry_id: str, device_registry: dr.DeviceRegistry, hub: BondHub) -> None: ...

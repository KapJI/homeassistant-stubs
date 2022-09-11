from .const import DOMAIN as DOMAIN, PLATFORMS as PLATFORMS
from .coordinator import TPLinkDataUpdateCoordinator as TPLinkDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant import config_entries as config_entries
from homeassistant.components import network as network
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_MAC as CONF_MAC, CONF_NAME as CONF_NAME, EVENT_HOMEASSISTANT_STARTED as EVENT_HOMEASSISTANT_STARTED
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers import discovery_flow as discovery_flow
from homeassistant.helpers.event import async_track_time_interval as async_track_time_interval
from homeassistant.helpers.typing import ConfigType as ConfigType
from kasa import SmartDevice as SmartDevice

DISCOVERY_INTERVAL: Incomplete

def async_trigger_discovery(hass: HomeAssistant, discovered_devices: dict[str, SmartDevice]) -> None: ...
async def async_discover_devices(hass: HomeAssistant) -> dict[str, SmartDevice]: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
def legacy_device_id(device: SmartDevice) -> str: ...

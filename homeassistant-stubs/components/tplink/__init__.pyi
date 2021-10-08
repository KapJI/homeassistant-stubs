from .const import CONF_DIMMER as CONF_DIMMER, CONF_DISCOVERY as CONF_DISCOVERY, CONF_LIGHT as CONF_LIGHT, CONF_STRIP as CONF_STRIP, CONF_SWITCH as CONF_SWITCH, DOMAIN as DOMAIN, PLATFORMS as PLATFORMS
from .coordinator import TPLinkDataUpdateCoordinator as TPLinkDataUpdateCoordinator
from .migration import async_migrate_entities_devices as async_migrate_entities_devices, async_migrate_legacy_entries as async_migrate_legacy_entries, async_migrate_yaml_entries as async_migrate_yaml_entries
from homeassistant import config_entries as config_entries
from homeassistant.components import network as network
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_MAC as CONF_MAC, CONF_NAME as CONF_NAME, EVENT_HOMEASSISTANT_STARTED as EVENT_HOMEASSISTANT_STARTED
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.event import async_track_time_interval as async_track_time_interval
from homeassistant.helpers.typing import ConfigType as ConfigType
from kasa import SmartDevice as SmartDevice
from typing import Any

DISCOVERY_INTERVAL: Any
TPLINK_HOST_SCHEMA: Any
CONFIG_SCHEMA: Any

def async_trigger_discovery(hass: HomeAssistant, discovered_devices: dict[str, SmartDevice]) -> None: ...
async def async_discover_devices(hass: HomeAssistant) -> dict[str, SmartDevice]: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
def async_entry_is_legacy(entry: ConfigEntry) -> bool: ...
def legacy_device_id(device: SmartDevice) -> str: ...

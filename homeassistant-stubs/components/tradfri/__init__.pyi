from .const import ATTR_TRADFRI_GATEWAY as ATTR_TRADFRI_GATEWAY, ATTR_TRADFRI_GATEWAY_MODEL as ATTR_TRADFRI_GATEWAY_MODEL, ATTR_TRADFRI_MANUFACTURER as ATTR_TRADFRI_MANUFACTURER, CONF_ALLOW_TRADFRI_GROUPS as CONF_ALLOW_TRADFRI_GROUPS, CONF_GATEWAY_ID as CONF_GATEWAY_ID, CONF_IDENTITY as CONF_IDENTITY, CONF_IMPORT_GROUPS as CONF_IMPORT_GROUPS, CONF_KEY as CONF_KEY, COORDINATOR as COORDINATOR, COORDINATOR_LIST as COORDINATOR_LIST, DEFAULT_ALLOW_TRADFRI_GROUPS as DEFAULT_ALLOW_TRADFRI_GROUPS, DOMAIN as DOMAIN, GROUPS_LIST as GROUPS_LIST, KEY_API as KEY_API, PLATFORMS as PLATFORMS, SIGNAL_GW as SIGNAL_GW, TIMEOUT_API as TIMEOUT_API
from .coordinator import TradfriDeviceDataUpdateCoordinator as TradfriDeviceDataUpdateCoordinator, TradfriGroupDataUpdateCoordinator as TradfriGroupDataUpdateCoordinator
from homeassistant import config_entries as config_entries
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect, async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.event import async_track_time_interval as async_track_time_interval
from homeassistant.helpers.typing import ConfigType as ConfigType
from pytradfri.command import Command as Command
from pytradfri.device import Device as Device
from pytradfri.group import Group as Group
from typing import Any

_LOGGER: Any
FACTORY: str
LISTENERS: str
CONFIG_SCHEMA: Any

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
def remove_stale_devices(hass: HomeAssistant, config_entry: ConfigEntry, devices: list[Device]) -> None: ...

from .const import CONNECTED_PLC_DEVICES as CONNECTED_PLC_DEVICES, CONNECTED_WIFI_CLIENTS as CONNECTED_WIFI_CLIENTS, DOMAIN as DOMAIN, LONG_UPDATE_INTERVAL as LONG_UPDATE_INTERVAL, NEIGHBORING_WIFI_NETWORKS as NEIGHBORING_WIFI_NETWORKS, PLATFORMS as PLATFORMS, SHORT_UPDATE_INTERVAL as SHORT_UPDATE_INTERVAL, SWITCH_GUEST_WIFI as SWITCH_GUEST_WIFI, SWITCH_LEDS as SWITCH_LEDS
from _typeshed import Incomplete
from devolo_plc_api.device_api import ConnectedStationInfo as ConnectedStationInfo, NeighborAPInfo as NeighborAPInfo, WifiGuestAccessGet as WifiGuestAccessGet
from devolo_plc_api.plcnet_api import LogicalNetwork as LogicalNetwork
from homeassistant.components import zeroconf as zeroconf
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_IP_ADDRESS as CONF_IP_ADDRESS, CONF_PASSWORD as CONF_PASSWORD, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.httpx_client import get_async_client as get_async_client
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

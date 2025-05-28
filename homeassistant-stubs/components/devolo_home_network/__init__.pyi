from .const import CONNECTED_PLC_DEVICES as CONNECTED_PLC_DEVICES, CONNECTED_WIFI_CLIENTS as CONNECTED_WIFI_CLIENTS, DOMAIN as DOMAIN, LAST_RESTART as LAST_RESTART, NEIGHBORING_WIFI_NETWORKS as NEIGHBORING_WIFI_NETWORKS, REGULAR_FIRMWARE as REGULAR_FIRMWARE, SWITCH_GUEST_WIFI as SWITCH_GUEST_WIFI, SWITCH_LEDS as SWITCH_LEDS
from .coordinator import DevoloDataUpdateCoordinator as DevoloDataUpdateCoordinator, DevoloFirmwareUpdateCoordinator as DevoloFirmwareUpdateCoordinator, DevoloHomeNetworkConfigEntry as DevoloHomeNetworkConfigEntry, DevoloHomeNetworkData as DevoloHomeNetworkData, DevoloLedSettingsGetCoordinator as DevoloLedSettingsGetCoordinator, DevoloLogicalNetworkCoordinator as DevoloLogicalNetworkCoordinator, DevoloUptimeGetCoordinator as DevoloUptimeGetCoordinator, DevoloWifiConnectedStationsGetCoordinator as DevoloWifiConnectedStationsGetCoordinator, DevoloWifiGuestAccessGetCoordinator as DevoloWifiGuestAccessGetCoordinator, DevoloWifiNeighborAPsGetCoordinator as DevoloWifiNeighborAPsGetCoordinator
from _typeshed import Incomplete
from devolo_plc_api import Device
from homeassistant.components import zeroconf as zeroconf
from homeassistant.const import CONF_IP_ADDRESS as CONF_IP_ADDRESS, CONF_PASSWORD as CONF_PASSWORD, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, Platform as Platform
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.httpx_client import get_async_client as get_async_client

_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: DevoloHomeNetworkConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: DevoloHomeNetworkConfigEntry) -> bool: ...
@callback
def platforms(device: Device) -> set[Platform]: ...

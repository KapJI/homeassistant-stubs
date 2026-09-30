from .const import CONF_SERIAL_NUMBER as CONF_SERIAL_NUMBER, DOMAIN as DOMAIN, PLATFORMS as PLATFORMS
from .models import LyngdorfConfigEntry as LyngdorfConfigEntry, LyngdorfRuntimeData as LyngdorfRuntimeData
from _typeshed import Incomplete
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_MODEL as CONF_MODEL, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC, DeviceInfo as DeviceInfo, async_get_device_id_by_identifier as async_get_device_id_by_identifier, format_mac as format_mac
from lyngdorf import LyngdorfReceiver as LyngdorfReceiver

_LOGGER: Incomplete

def _serial_as_mac(serial: str) -> str | None: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: LyngdorfConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, config_entry: LyngdorfConfigEntry) -> bool: ...

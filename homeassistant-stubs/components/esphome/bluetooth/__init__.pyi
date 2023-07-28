from ..entry_data import RuntimeEntryData as RuntimeEntryData
from .cache import ESPHomeBluetoothCache as ESPHomeBluetoothCache
from .client import ESPHomeClient as ESPHomeClient, ESPHomeClientData as ESPHomeClientData
from .device import ESPHomeBluetoothDevice as ESPHomeBluetoothDevice
from .scanner import ESPHomeScanner as ESPHomeScanner
from _typeshed import Incomplete
from aioesphomeapi import APIClient as APIClient
from homeassistant.components.bluetooth import HaBluetoothConnector as HaBluetoothConnector, async_get_advertisement_callback as async_get_advertisement_callback, async_register_scanner as async_register_scanner
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant

_LOGGER: Incomplete

def _async_can_connect(entry_data: RuntimeEntryData, bluetooth_device: ESPHomeBluetoothDevice, source: str) -> bool: ...
async def async_connect_scanner(hass: HomeAssistant, entry: ConfigEntry, cli: APIClient, entry_data: RuntimeEntryData, cache: ESPHomeBluetoothCache) -> CALLBACK_TYPE: ...

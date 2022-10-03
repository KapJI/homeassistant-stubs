from ..domain_data import DomainData as DomainData
from ..entry_data import RuntimeEntryData as RuntimeEntryData
from .client import ESPHomeClient as ESPHomeClient
from .scanner import ESPHomeScanner as ESPHomeScanner
from _typeshed import Incomplete
from aioesphomeapi import APIClient as APIClient
from homeassistant.components.bluetooth import HaBluetoothConnector as HaBluetoothConnector, async_get_advertisement_callback as async_get_advertisement_callback, async_register_scanner as async_register_scanner
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant, async_get_hass as async_get_hass

_LOGGER: Incomplete

def async_can_connect(source: str) -> bool: ...
async def async_connect_scanner(hass: HomeAssistant, entry: ConfigEntry, cli: APIClient, entry_data: RuntimeEntryData) -> CALLBACK_TYPE: ...

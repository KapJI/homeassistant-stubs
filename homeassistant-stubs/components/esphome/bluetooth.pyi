from .const import CONF_BLUETOOTH_SCANNING_MODE as CONF_BLUETOOTH_SCANNING_MODE, DEFAULT_BLUETOOTH_SCANNING_MODE as DEFAULT_BLUETOOTH_SCANNING_MODE, DOMAIN as DOMAIN
from .entry_data import ESPHomeConfigEntry as ESPHomeConfigEntry, RuntimeEntryData as RuntimeEntryData
from _typeshed import Incomplete
from aioesphomeapi import APIClient as APIClient, BluetoothScannerStateResponse as BluetoothScannerStateResponse, DeviceInfo as DeviceInfo
from bleak_esphome.backend.scanner import ESPHomeScanner as ESPHomeScanner
from homeassistant.components.bluetooth import BluetoothScanningMode as BluetoothScanningMode, async_register_scanner as async_register_scanner
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant, callback as hass_callback

_LOGGER: Incomplete
_VALID_SCANNING_MODES: Incomplete

@hass_callback
def _async_unload(unload_callbacks: list[CALLBACK_TYPE]) -> None: ...
@hass_callback
def async_connect_scanner(hass: HomeAssistant, entry: ESPHomeConfigEntry, entry_data: RuntimeEntryData, cli: APIClient, device_info: DeviceInfo, device_id: str) -> CALLBACK_TYPE: ...
@hass_callback
def _async_apply_scanning_mode(hass: HomeAssistant, entry: ESPHomeConfigEntry, scanner: ESPHomeScanner, cli: APIClient) -> CALLBACK_TYPE | None: ...

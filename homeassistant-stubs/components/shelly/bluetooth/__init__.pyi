from ..const import BLEScannerMode as BLEScannerMode
from ..coordinator import ShellyRpcCoordinator as ShellyRpcCoordinator
from .scanner import ShellyBLEScanner as ShellyBLEScanner
from homeassistant.components.bluetooth import HaBluetoothConnector as HaBluetoothConnector, async_get_advertisement_callback as async_get_advertisement_callback, async_register_scanner as async_register_scanner
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import format_mac as format_mac

async def async_connect_scanner(hass: HomeAssistant, coordinator: ShellyRpcCoordinator, scanner_mode: BLEScannerMode) -> CALLBACK_TYPE: ...

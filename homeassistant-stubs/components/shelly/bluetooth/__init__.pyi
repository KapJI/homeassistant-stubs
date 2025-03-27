from ..const import BLEScannerMode as BLEScannerMode
from ..coordinator import ShellyRpcCoordinator as ShellyRpcCoordinator
from _typeshed import Incomplete
from homeassistant.components.bluetooth import BluetoothScanningMode as BluetoothScanningMode, async_register_scanner as async_register_scanner
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant

BLE_SCANNER_MODE_TO_BLUETOOTH_SCANNING_MODE: Incomplete

async def async_connect_scanner(hass: HomeAssistant, coordinator: ShellyRpcCoordinator, scanner_mode: BLEScannerMode, device_id: str) -> CALLBACK_TYPE: ...

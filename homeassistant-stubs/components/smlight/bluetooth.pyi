from .const import BLEScannerMode as BLEScannerMode, CONF_BLE_SCANNER_MODE as CONF_BLE_SCANNER_MODE, DOMAIN as DOMAIN
from .coordinator import SmConfigEntry as SmConfigEntry, base_device_info as base_device_info
from _typeshed import Incomplete
from homeassistant.components.bluetooth import BluetoothScanningMode as BluetoothScanningMode, async_register_scanner as async_register_scanner
from homeassistant.const import CONF_HOST as CONF_HOST
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant, callback as callback
from pysmlight import Api2 as Api2, BleProxyClient as BleProxyClient, Info as Info

_LOGGER: Incomplete

@callback
def _async_unload(unload_callbacks: list[CALLBACK_TYPE], client: BleProxyClient) -> None: ...
@callback
def async_connect_scanner(hass: HomeAssistant, entry: SmConfigEntry, model: str | None, device_id: str, scanner_mode: BluetoothScanningMode = ...) -> CALLBACK_TYPE: ...
async def async_setup_ble_scanner(hass: HomeAssistant, entry: SmConfigEntry, client: Api2, info: Info) -> CALLBACK_TYPE | None: ...
@callback
def get_ble_scanner_mode(entry: SmConfigEntry, info: Info) -> BLEScannerMode: ...

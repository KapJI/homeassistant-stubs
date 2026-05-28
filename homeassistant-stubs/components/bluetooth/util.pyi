from .const import CONF_MODE as CONF_MODE, CONF_PASSIVE as CONF_PASSIVE, DEFAULT_MODE as DEFAULT_MODE
from .models import BluetoothServiceInfoBleak as BluetoothServiceInfoBleak
from .storage import BluetoothStorage as BluetoothStorage
from _typeshed import Incomplete
from bluetooth_adapters import AdapterDetails as AdapterDetails, BluetoothAdapters as BluetoothAdapters
from collections.abc import Mapping
from habluetooth import BluetoothScanningMode
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from typing import Any

_LOGGER: Incomplete

def resolve_scanning_mode(options: Mapping[str, Any]) -> BluetoothScanningMode: ...

class InvalidConfigEntryID(HomeAssistantError): ...
class InvalidSource(HomeAssistantError): ...

@callback
def async_load_history_from_system(adapters: BluetoothAdapters, storage: BluetoothStorage) -> tuple[dict[str, BluetoothServiceInfoBleak], dict[str, BluetoothServiceInfoBleak]]: ...
@callback
def adapter_title(adapter: str, details: AdapterDetails) -> str: ...
def config_entry_id_to_source(hass: HomeAssistant, config_entry_id: str) -> str: ...

from .models import BluetoothServiceInfoBleak as BluetoothServiceInfoBleak
from .storage import BluetoothStorage as BluetoothStorage
from bluetooth_adapters import BluetoothAdapters as BluetoothAdapters
from homeassistant.core import callback as callback

def async_load_history_from_system(adapters: BluetoothAdapters, storage: BluetoothStorage) -> tuple[dict[str, BluetoothServiceInfoBleak], dict[str, BluetoothServiceInfoBleak]]: ...

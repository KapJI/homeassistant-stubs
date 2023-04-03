from .models import BluetoothServiceInfoBleak as BluetoothServiceInfoBleak
from .storage import BluetoothStorage as BluetoothStorage
from bluetooth_adapters import BluetoothAdapters as BluetoothAdapters
from homeassistant.core import callback as callback
from homeassistant.util.dt import monotonic_time_coarse as monotonic_time_coarse

def async_load_history_from_system(adapters: BluetoothAdapters, storage: BluetoothStorage) -> tuple[dict[str, BluetoothServiceInfoBleak], dict[str, BluetoothServiceInfoBleak]]: ...
async def async_reset_adapter(adapter: str | None, mac_address: str) -> bool | None: ...

from .manager import HomeAssistantBluetoothManager as HomeAssistantBluetoothManager
from _typeshed import Incomplete
from collections.abc import Callable
from home_assistant_bluetooth import BluetoothServiceInfoBleak

MANAGER: HomeAssistantBluetoothManager | None
BluetoothChange: Incomplete
BluetoothCallback = Callable[[BluetoothServiceInfoBleak, BluetoothChange], None]
ProcessAdvertisementCallback = Callable[[BluetoothServiceInfoBleak], bool]

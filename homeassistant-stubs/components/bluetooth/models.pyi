from _typeshed import Incomplete
from collections.abc import Callable
from enum import Enum
from home_assistant_bluetooth import BluetoothServiceInfoBleak

BluetoothChange: Incomplete
type BluetoothCallback = Callable[[BluetoothServiceInfoBleak, BluetoothChange], None]
type ProcessAdvertisementCallback = Callable[[BluetoothServiceInfoBleak], bool]

class BluetoothCallbackReplay(Enum):
    OLDEST_FIRST = ...
    NEWEST_FIRST = ...
    DISABLED = ...

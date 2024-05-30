from _typeshed import Incomplete
from collections.abc import Callable
from home_assistant_bluetooth import BluetoothServiceInfoBleak

BluetoothChange: Incomplete
BluetoothCallback = Callable[[BluetoothServiceInfoBleak, BluetoothChange], None]
ProcessAdvertisementCallback = Callable[[BluetoothServiceInfoBleak], bool]

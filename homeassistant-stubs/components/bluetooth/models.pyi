from .manager import BluetoothManager as BluetoothManager
from _typeshed import Incomplete
from bleak import BaseBleakClient as BaseBleakClient
from collections.abc import Callable
from enum import Enum
from home_assistant_bluetooth import BluetoothServiceInfoBleak
from homeassistant.util.dt import monotonic_time_coarse as monotonic_time_coarse
from typing import Final

MANAGER: Union[BluetoothManager, None]
MONOTONIC_TIME: Final[Incomplete]

class HaBluetoothConnector:
    client: type[BaseBleakClient]
    source: str
    can_connect: Callable[[], bool]
    def __init__(self, client, source, can_connect) -> None: ...

class BluetoothScanningMode(Enum):
    PASSIVE: str
    ACTIVE: str

BluetoothChange: Incomplete
BluetoothCallback = Callable[[BluetoothServiceInfoBleak, BluetoothChange], None]
ProcessAdvertisementCallback = Callable[[BluetoothServiceInfoBleak], bool]

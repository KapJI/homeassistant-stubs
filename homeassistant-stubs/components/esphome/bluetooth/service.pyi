from _typeshed import Incomplete
from aioesphomeapi.model import BluetoothGATTService as BluetoothGATTService
from bleak.backends.characteristic import BleakGATTCharacteristic as BleakGATTCharacteristic
from bleak.backends.service import BleakGATTService

class BleakGATTServiceESPHome(BleakGATTService):
    obj: BluetoothGATTService
    __characteristics: Incomplete
    __handle: Incomplete
    def __init__(self, obj: BluetoothGATTService) -> None: ...
    @property
    def handle(self) -> int: ...
    @property
    def uuid(self) -> str: ...
    @property
    def characteristics(self) -> list[BleakGATTCharacteristic]: ...
    def add_characteristic(self, characteristic: BleakGATTCharacteristic) -> None: ...

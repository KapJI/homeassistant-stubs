from _typeshed import Incomplete
from aioesphomeapi.model import BluetoothGATTDescriptor as BluetoothGATTDescriptor
from bleak.backends.descriptor import BleakGATTDescriptor

class BleakGATTDescriptorESPHome(BleakGATTDescriptor):
    obj: BluetoothGATTDescriptor
    __characteristic_uuid: Incomplete
    __characteristic_handle: Incomplete
    def __init__(self, obj: BluetoothGATTDescriptor, characteristic_uuid: str, characteristic_handle: int) -> None: ...
    @property
    def characteristic_handle(self) -> int: ...
    @property
    def characteristic_uuid(self) -> str: ...
    @property
    def uuid(self) -> str: ...
    @property
    def handle(self) -> int: ...

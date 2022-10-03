from _typeshed import Incomplete
from aioesphomeapi.model import BluetoothGATTCharacteristic as BluetoothGATTCharacteristic
from bleak.backends.characteristic import BleakGATTCharacteristic
from bleak.backends.descriptor import BleakGATTDescriptor as BleakGATTDescriptor
from uuid import UUID

PROPERTY_MASKS: Incomplete

class BleakGATTCharacteristicESPHome(BleakGATTCharacteristic):
    obj: BluetoothGATTCharacteristic
    __descriptors: Incomplete
    __service_uuid: Incomplete
    __service_handle: Incomplete
    __props: Incomplete
    def __init__(self, obj: BluetoothGATTCharacteristic, max_write_without_response_size: int, service_uuid: str, service_handle: int) -> None: ...
    @property
    def service_uuid(self) -> str: ...
    @property
    def service_handle(self) -> int: ...
    @property
    def handle(self) -> int: ...
    @property
    def uuid(self) -> str: ...
    @property
    def properties(self) -> list[str]: ...
    @property
    def descriptors(self) -> list[BleakGATTDescriptor]: ...
    def get_descriptor(self, specifier: Union[int, str, UUID]) -> Union[BleakGATTDescriptor, None]: ...
    def add_descriptor(self, descriptor: BleakGATTDescriptor) -> None: ...

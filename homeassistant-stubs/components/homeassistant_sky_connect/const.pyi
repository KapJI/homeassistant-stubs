import dataclasses
import enum
from _typeshed import Incomplete
from typing import Self

DOMAIN: str

@dataclasses.dataclass(frozen=True)
class VariantInfo:
    usb_product_name: str
    short_name: str
    full_name: str
    def __init__(self, usb_product_name, short_name, full_name) -> None: ...

class HardwareVariant(VariantInfo, enum.Enum):
    SKYCONNECT: Incomplete
    CONNECT_ZBT1: Incomplete
    @classmethod
    def from_usb_product_name(cls, usb_product_name: str) -> Self: ...

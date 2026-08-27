from dataclasses import dataclass
from typing import Literal

@dataclass(slots=True, frozen=True, kw_only=True)
class SerialDevice:
    device: str
    resolved_device: str | None = ...
    serial_number: str | None
    manufacturer: str | None
    description: str | None
    interface_description: str | None = ...
    interface_num: int | None = ...

@dataclass(slots=True, frozen=True, kw_only=True)
class USBDevice(SerialDevice):
    vid: str
    pid: str
    bcd_device: int | None = ...

@dataclass(slots=True, frozen=True, kw_only=True)
class SerialPortConsumer:
    kind: Literal['config_entry', 'app']
    title: str
    active: bool
    domain: str | None = ...
    config_entry_id: str | None = ...
    slug: str | None = ...

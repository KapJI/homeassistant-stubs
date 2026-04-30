from dataclasses import dataclass

@dataclass(slots=True, frozen=True, kw_only=True)
class SerialDevice:
    device: str
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

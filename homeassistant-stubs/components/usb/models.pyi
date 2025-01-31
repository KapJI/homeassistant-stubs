from dataclasses import dataclass

@dataclass(slots=True, frozen=True, kw_only=True)
class USBDevice:
    device: str
    vid: str
    pid: str
    serial_number: str | None
    manufacturer: str | None
    description: str | None

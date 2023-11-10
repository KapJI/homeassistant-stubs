from dataclasses import dataclass

@dataclass
class USBDevice:
    device: str
    vid: str
    pid: str
    serial_number: str | None
    manufacturer: str | None
    description: str | None
    def __init__(self, device, vid, pid, serial_number, manufacturer, description) -> None: ...

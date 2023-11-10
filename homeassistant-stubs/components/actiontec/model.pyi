from dataclasses import dataclass

@dataclass
class Device:
    ip_address: str
    mac_address: str
    timevalid: int
    def __init__(self, ip_address, mac_address, timevalid) -> None: ...

from typing import Any

class Device:
    ip_address: str
    mac_address: str
    timevalid: int
    def __init__(self, ip_address: Any, mac_address: Any, timevalid: Any) -> None: ...

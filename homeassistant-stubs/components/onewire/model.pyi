from dataclasses import dataclass
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo

@dataclass
class OWDeviceDescription:
    device_info: DeviceInfo
    family: str
    id: str
    path: str
    type: str
    def __init__(self, device_info, family, id, path, type) -> None: ...

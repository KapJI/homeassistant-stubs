from homeassistant.helpers.entity import DeviceInfo as DeviceInfo

class OWDeviceDescription:
    device_info: DeviceInfo
    family: str
    id: str
    path: str
    type: str
    def __init__(self, device_info, family, id, path, type) -> None: ...

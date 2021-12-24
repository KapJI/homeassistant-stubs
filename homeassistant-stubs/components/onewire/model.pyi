from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from pi1wire import OneWireInterface as OneWireInterface

class OWDeviceDescription:
    device_info: DeviceInfo
    def __init__(self, device_info) -> None: ...

class OWDirectDeviceDescription(OWDeviceDescription):
    interface: OneWireInterface
    def __init__(self, device_info, interface) -> None: ...

class OWServerDeviceDescription(OWDeviceDescription):
    family: str
    id: str
    path: str
    type: str
    def __init__(self, device_info, family, id, path, type) -> None: ...

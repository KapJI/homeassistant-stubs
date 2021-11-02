from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from pi1wire import OneWireInterface as OneWireInterface

class OWDeviceDescription:
    device_info: DeviceInfo

class OWDirectDeviceDescription(OWDeviceDescription):
    interface: OneWireInterface

class OWServerDeviceDescription(OWDeviceDescription):
    family: str
    id: str
    path: str
    type: str

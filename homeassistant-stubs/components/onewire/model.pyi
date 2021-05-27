from typing import TypedDict

class DeviceComponentDescription(TypedDict):
    path: str
    name: str
    type: str
    default_disabled: bool

class OWServerDeviceDescription(TypedDict):
    path: str
    family: str
    type: str

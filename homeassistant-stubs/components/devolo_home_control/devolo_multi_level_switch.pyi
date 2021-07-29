from .devolo_device import DevoloDeviceEntity as DevoloDeviceEntity
from devolo_home_control_api.devices.zwave import Zwave as Zwave
from devolo_home_control_api.homecontrol import HomeControl as HomeControl
from typing import Any

class DevoloMultiLevelSwitchDeviceEntity(DevoloDeviceEntity):
    _multi_level_switch_property: Any
    _value: Any
    def __init__(self, homecontrol: HomeControl, device_instance: Zwave, element_uid: str) -> None: ...

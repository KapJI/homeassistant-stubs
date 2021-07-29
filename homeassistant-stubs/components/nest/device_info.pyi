from .const import DOMAIN as DOMAIN
from google_nest_sdm.device import Device as Device
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from typing import Any

DEVICE_TYPE_MAP: dict[str, str]

class NestDeviceInfo:
    device_brand: str
    _device: Any
    def __init__(self, device: Device) -> None: ...
    @property
    def device_info(self) -> DeviceInfo: ...
    @property
    def device_name(self) -> str: ...
    @property
    def device_model(self) -> str: ...

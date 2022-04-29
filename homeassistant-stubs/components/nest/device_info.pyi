from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from google_nest_sdm.device import Device as Device
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo

DEVICE_TYPE_MAP: dict[str, str]

class NestDeviceInfo:
    device_brand: str
    _device: Incomplete
    def __init__(self, device: Device) -> None: ...
    @property
    def device_info(self) -> DeviceInfo: ...
    @property
    def device_name(self) -> Union[str, None]: ...
    @property
    def device_model(self) -> Union[str, None]: ...
    @property
    def suggested_area(self) -> Union[str, None]: ...

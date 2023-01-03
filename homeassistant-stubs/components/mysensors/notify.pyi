from .. import mysensors as mysensors
from .const import DevId as DevId, DiscoveryInfo as DiscoveryInfo
from _typeshed import Incomplete
from homeassistant.components.notify import ATTR_TARGET as ATTR_TARGET, BaseNotificationService as BaseNotificationService
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

async def async_get_service(hass: HomeAssistant, config: ConfigType, discovery_info: Union[DiscoveryInfoType, None] = ...) -> Union[BaseNotificationService, None]: ...

class MySensorsNotificationDevice(mysensors.device.MySensorsDevice):
    def send_msg(self, msg: str) -> None: ...
    def __repr__(self) -> str: ...

class MySensorsNotificationService(BaseNotificationService):
    devices: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    async def async_send_message(self, message: str = ..., **kwargs: Any) -> None: ...

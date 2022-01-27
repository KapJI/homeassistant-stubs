from .const import DevId as DevId, DiscoveryInfo as DiscoveryInfo
from homeassistant.components import mysensors as mysensors
from homeassistant.components.notify import ATTR_TARGET as ATTR_TARGET, BaseNotificationService as BaseNotificationService
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

async def async_get_service(hass: HomeAssistant, config: dict[str, Any], discovery_info: Union[DiscoveryInfo, None] = ...) -> Union[BaseNotificationService, None]: ...

class MySensorsNotificationDevice(mysensors.device.MySensorsDevice):
    def send_msg(self, msg: str) -> None: ...
    def __repr__(self) -> str: ...

class MySensorsNotificationService(BaseNotificationService):
    devices: Any
    def __init__(self, hass: HomeAssistant) -> None: ...
    async def async_send_message(self, message: str = ..., **kwargs: Any) -> None: ...

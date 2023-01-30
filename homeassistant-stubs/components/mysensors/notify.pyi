from .. import mysensors as mysensors
from .const import DOMAIN as DOMAIN, DevId as DevId, DiscoveryInfo as DiscoveryInfo
from _typeshed import Incomplete
from homeassistant.components.notify import ATTR_TARGET as ATTR_TARGET, BaseNotificationService as BaseNotificationService
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.issue_registry import IssueSeverity as IssueSeverity, async_create_issue as async_create_issue
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from homeassistant.util import slugify as slugify
from typing import Any

async def async_get_service(hass: HomeAssistant, config: ConfigType, discovery_info: Union[DiscoveryInfoType, None] = ...) -> Union[BaseNotificationService, None]: ...

class MySensorsNotificationDevice(mysensors.device.MySensorsDevice):
    def _async_update_callback(self) -> None: ...
    def send_msg(self, msg: str) -> None: ...
    def __repr__(self) -> str: ...

class MySensorsNotificationService(BaseNotificationService):
    devices: Incomplete
    hass: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    async def async_send_message(self, message: str = ..., **kwargs: Any) -> None: ...

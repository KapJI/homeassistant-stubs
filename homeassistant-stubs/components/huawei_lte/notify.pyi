from . import Router as Router
from .const import ATTR_UNIQUE_ID as ATTR_UNIQUE_ID, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.notify import ATTR_TARGET as ATTR_TARGET, BaseNotificationService as BaseNotificationService
from homeassistant.const import CONF_RECIPIENT as CONF_RECIPIENT
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

_LOGGER: Incomplete

async def async_get_service(hass: HomeAssistant, config: ConfigType, discovery_info: Union[DiscoveryInfoType, None] = ...) -> Union[HuaweiLteSmsNotificationService, None]: ...

class HuaweiLteSmsNotificationService(BaseNotificationService):
    router: Router
    default_targets: list[str]
    def send_message(self, message: str = ..., **kwargs: Any) -> None: ...
    def __init__(self, router, default_targets) -> None: ...

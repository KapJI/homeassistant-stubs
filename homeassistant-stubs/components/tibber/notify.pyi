from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.components.notify import ATTR_TITLE as ATTR_TITLE, ATTR_TITLE_DEFAULT as ATTR_TITLE_DEFAULT, BaseNotificationService as BaseNotificationService
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

_LOGGER: Incomplete

async def async_get_service(hass: HomeAssistant, config: ConfigType, discovery_info: Union[DiscoveryInfoType, None] = ...) -> TibberNotificationService: ...

class TibberNotificationService(BaseNotificationService):
    _notify: Incomplete
    def __init__(self, notify: Callable) -> None: ...
    async def async_send_message(self, message: str = ..., **kwargs: Any) -> None: ...

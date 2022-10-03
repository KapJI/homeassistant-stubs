from _typeshed import Incomplete
from homeassistant.components.notify import BaseNotificationService as BaseNotificationService
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

EVENT_NOTIFY: str

def get_service(hass: HomeAssistant, config: ConfigType, discovery_info: Union[DiscoveryInfoType, None] = ...) -> BaseNotificationService: ...

class DemoNotificationService(BaseNotificationService):
    hass: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    @property
    def targets(self) -> dict[str, str]: ...
    def send_message(self, message: str = ..., **kwargs: Any) -> None: ...

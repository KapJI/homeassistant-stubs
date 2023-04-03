from _typeshed import Incomplete
from homeassistant.components.notify import ATTR_DATA as ATTR_DATA, ATTR_MESSAGE as ATTR_MESSAGE, BaseNotificationService as BaseNotificationService, DOMAIN as DOMAIN, PLATFORM_SCHEMA as PLATFORM_SCHEMA
from homeassistant.const import ATTR_SERVICE as ATTR_SERVICE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

CONF_SERVICES: str

def add_defaults(input_data: dict[str, Any], default_data: dict[str, Any]) -> dict[str, Any]: ...
async def async_get_service(hass: HomeAssistant, config: ConfigType, discovery_info: DiscoveryInfoType | None = ...) -> GroupNotifyPlatform: ...

class GroupNotifyPlatform(BaseNotificationService):
    hass: Incomplete
    entities: Incomplete
    def __init__(self, hass: HomeAssistant, entities: list[dict[str, Any]]) -> None: ...
    async def async_send_message(self, message: str = ..., **kwargs: Any) -> None: ...

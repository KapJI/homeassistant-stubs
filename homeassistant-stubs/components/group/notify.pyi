from homeassistant.components.notify import ATTR_DATA as ATTR_DATA, ATTR_MESSAGE as ATTR_MESSAGE, BaseNotificationService as BaseNotificationService, DOMAIN as DOMAIN, PLATFORM_SCHEMA as PLATFORM_SCHEMA
from homeassistant.const import ATTR_SERVICE as ATTR_SERVICE
from typing import Any

CONF_SERVICES: str

def update(input_dict, update_source): ...
async def async_get_service(hass, config, discovery_info: Any | None = ...): ...

class GroupNotifyPlatform(BaseNotificationService):
    hass: Any
    entities: Any
    def __init__(self, hass, entities) -> None: ...
    async def async_send_message(self, message: str = ..., **kwargs) -> None: ...

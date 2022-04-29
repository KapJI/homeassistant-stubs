from _typeshed import Incomplete
from homeassistant.components.notify import ATTR_DATA as ATTR_DATA, ATTR_MESSAGE as ATTR_MESSAGE, BaseNotificationService as BaseNotificationService, DOMAIN as DOMAIN, PLATFORM_SCHEMA as PLATFORM_SCHEMA
from homeassistant.const import ATTR_SERVICE as ATTR_SERVICE

CONF_SERVICES: str

def update(input_dict, update_source): ...
async def async_get_service(hass, config, discovery_info: Incomplete | None = ...): ...

class GroupNotifyPlatform(BaseNotificationService):
    hass: Incomplete
    entities: Incomplete
    def __init__(self, hass, entities) -> None: ...
    async def async_send_message(self, message: str = ..., **kwargs) -> None: ...

from . import ATTR_LANGUAGE as ATTR_LANGUAGE, ATTR_MESSAGE as ATTR_MESSAGE, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.notify import BaseNotificationService as BaseNotificationService, PLATFORM_SCHEMA as PLATFORM_SCHEMA
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, CONF_NAME as CONF_NAME
from homeassistant.core import split_entity_id as split_entity_id

CONF_MEDIA_PLAYER: str
CONF_TTS_SERVICE: str
_LOGGER: Incomplete

async def async_get_service(hass, config, discovery_info: Incomplete | None = ...): ...

class TTSNotificationService(BaseNotificationService):
    _media_player: Incomplete
    _language: Incomplete
    def __init__(self, config) -> None: ...
    async def async_send_message(self, message: str = ..., **kwargs) -> None: ...

from . import ATTR_ENTITY_ID as ATTR_ENTITY_ID, ATTR_LANGUAGE as ATTR_LANGUAGE, ATTR_MESSAGE as ATTR_MESSAGE, DOMAIN as DOMAIN
from homeassistant.components.notify import BaseNotificationService as BaseNotificationService, PLATFORM_SCHEMA as PLATFORM_SCHEMA
from homeassistant.const import CONF_NAME as CONF_NAME
from homeassistant.core import split_entity_id as split_entity_id
from typing import Any, Optional

CONF_MEDIA_PLAYER: str
CONF_TTS_SERVICE: str
_LOGGER: Any

async def async_get_service(hass: Any, config: Any, discovery_info: Optional[Any] = ...): ...

class TTSNotificationService(BaseNotificationService):
    _media_player: Any = ...
    _language: Any = ...
    def __init__(self, config: Any) -> None: ...
    async def async_send_message(self, message: str = ..., **kwargs: Any) -> None: ...

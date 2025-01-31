from . import WebOsTvConfigEntry as WebOsTvConfigEntry
from .const import ATTR_CONFIG_ENTRY_ID as ATTR_CONFIG_ENTRY_ID, DOMAIN as DOMAIN, WEBOSTV_EXCEPTIONS as WEBOSTV_EXCEPTIONS
from _typeshed import Incomplete
from aiowebostv import WebOsClient as WebOsClient
from homeassistant.components.notify import ATTR_DATA as ATTR_DATA, BaseNotificationService as BaseNotificationService
from homeassistant.const import ATTR_ICON as ATTR_ICON
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

PARALLEL_UPDATES: int

async def async_get_service(hass: HomeAssistant, config: ConfigType, discovery_info: DiscoveryInfoType | None = None) -> BaseNotificationService | None: ...

class LgWebOSNotificationService(BaseNotificationService):
    _entry: Incomplete
    def __init__(self, entry: WebOsTvConfigEntry) -> None: ...
    async def async_send_message(self, message: str = '', **kwargs: Any) -> None: ...

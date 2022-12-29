from .const import CONF_BASE_URL as CONF_BASE_URL, DEFAULT_URL as DEFAULT_URL, LOGGER as LOGGER
from _typeshed import Incomplete
from homeassistant.components.notify import BaseNotificationService as BaseNotificationService, PLATFORM_SCHEMA as PLATFORM_SCHEMA
from homeassistant.const import CONF_ACCESS_TOKEN as CONF_ACCESS_TOKEN, CONF_CLIENT_ID as CONF_CLIENT_ID, CONF_CLIENT_SECRET as CONF_CLIENT_SECRET
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from mastodon import Mastodon
from typing import Any

def get_service(hass: HomeAssistant, config: ConfigType, discovery_info: Union[DiscoveryInfoType, None] = ...) -> Union[MastodonNotificationService, None]: ...

class MastodonNotificationService(BaseNotificationService):
    _api: Incomplete
    def __init__(self, api: Mastodon) -> None: ...
    def send_message(self, message: str = ..., **kwargs: Any) -> None: ...

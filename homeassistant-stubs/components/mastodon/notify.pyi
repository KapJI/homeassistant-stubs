from .const import CONF_BASE_URL as CONF_BASE_URL, DEFAULT_URL as DEFAULT_URL, LOGGER as LOGGER
from _typeshed import Incomplete
from homeassistant.components.notify import ATTR_DATA as ATTR_DATA, BaseNotificationService as BaseNotificationService
from homeassistant.const import CONF_ACCESS_TOKEN as CONF_ACCESS_TOKEN, CONF_CLIENT_ID as CONF_CLIENT_ID, CONF_CLIENT_SECRET as CONF_CLIENT_SECRET
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from mastodon import Mastodon
from typing import Any

ATTR_MEDIA: str
ATTR_TARGET: str
ATTR_MEDIA_WARNING: str
ATTR_CONTENT_WARNING: str
PLATFORM_SCHEMA: Incomplete

def get_service(hass: HomeAssistant, config: ConfigType, discovery_info: DiscoveryInfoType | None = None) -> MastodonNotificationService | None: ...

class MastodonNotificationService(BaseNotificationService):
    _api: Incomplete
    def __init__(self, api: Mastodon) -> None: ...
    def send_message(self, message: str = '', **kwargs: Any) -> None: ...
    def _upload_media(self, media_path: Any = None) -> Any: ...
    def _media_type(self, media_path: Any = None) -> Any: ...

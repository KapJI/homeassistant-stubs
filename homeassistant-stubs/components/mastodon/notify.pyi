from .const import ATTR_CONTENT_WARNING as ATTR_CONTENT_WARNING, ATTR_MEDIA_WARNING as ATTR_MEDIA_WARNING, CONF_BASE_URL as CONF_BASE_URL, DEFAULT_URL as DEFAULT_URL, DOMAIN as DOMAIN
from .utils import get_media_type as get_media_type
from _typeshed import Incomplete
from homeassistant.components.notify import ATTR_DATA as ATTR_DATA, BaseNotificationService as BaseNotificationService
from homeassistant.const import CONF_ACCESS_TOKEN as CONF_ACCESS_TOKEN, CONF_CLIENT_ID as CONF_CLIENT_ID, CONF_CLIENT_SECRET as CONF_CLIENT_SECRET
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from mastodon import Mastodon
from mastodon.Mastodon import MediaAttachment as MediaAttachment
from typing import Any

ATTR_MEDIA: str
ATTR_TARGET: str
PLATFORM_SCHEMA: Incomplete
INTEGRATION_TITLE: str

async def async_get_service(hass: HomeAssistant, config: ConfigType, discovery_info: DiscoveryInfoType | None = None) -> MastodonNotificationService | None: ...

class MastodonNotificationService(BaseNotificationService):
    client: Incomplete
    def __init__(self, hass: HomeAssistant, client: Mastodon) -> None: ...
    def send_message(self, message: str = '', **kwargs: Any) -> None: ...
    def _upload_media(self, media_path: Any = None) -> MediaAttachment: ...

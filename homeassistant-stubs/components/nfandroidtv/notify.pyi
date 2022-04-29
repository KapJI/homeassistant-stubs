from .const import ATTR_COLOR as ATTR_COLOR, ATTR_DURATION as ATTR_DURATION, ATTR_FONTSIZE as ATTR_FONTSIZE, ATTR_ICON as ATTR_ICON, ATTR_ICON_AUTH as ATTR_ICON_AUTH, ATTR_ICON_AUTH_DIGEST as ATTR_ICON_AUTH_DIGEST, ATTR_ICON_PASSWORD as ATTR_ICON_PASSWORD, ATTR_ICON_PATH as ATTR_ICON_PATH, ATTR_ICON_URL as ATTR_ICON_URL, ATTR_ICON_USERNAME as ATTR_ICON_USERNAME, ATTR_IMAGE as ATTR_IMAGE, ATTR_IMAGE_AUTH as ATTR_IMAGE_AUTH, ATTR_IMAGE_AUTH_DIGEST as ATTR_IMAGE_AUTH_DIGEST, ATTR_IMAGE_PASSWORD as ATTR_IMAGE_PASSWORD, ATTR_IMAGE_PATH as ATTR_IMAGE_PATH, ATTR_IMAGE_URL as ATTR_IMAGE_URL, ATTR_IMAGE_USERNAME as ATTR_IMAGE_USERNAME, ATTR_INTERRUPT as ATTR_INTERRUPT, ATTR_POSITION as ATTR_POSITION, ATTR_TRANSPARENCY as ATTR_TRANSPARENCY, CONF_COLOR as CONF_COLOR, CONF_DURATION as CONF_DURATION, CONF_FONTSIZE as CONF_FONTSIZE, CONF_INTERRUPT as CONF_INTERRUPT, CONF_POSITION as CONF_POSITION, CONF_TRANSPARENCY as CONF_TRANSPARENCY, DEFAULT_TIMEOUT as DEFAULT_TIMEOUT
from _typeshed import Incomplete
from homeassistant.components.notify import ATTR_DATA as ATTR_DATA, ATTR_TITLE as ATTR_TITLE, ATTR_TITLE_DEFAULT as ATTR_TITLE_DEFAULT, BaseNotificationService as BaseNotificationService, PLATFORM_SCHEMA as PLATFORM_SCHEMA
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_TIMEOUT as CONF_TIMEOUT
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from io import BufferedReader
from notifications_android_tv import Notifications
from typing import Any

_LOGGER: Incomplete

async def async_get_service(hass: HomeAssistant, config: ConfigType, discovery_info: Union[DiscoveryInfoType, None] = ...) -> NFAndroidTVNotificationService: ...

class NFAndroidTVNotificationService(BaseNotificationService):
    notify: Incomplete
    is_allowed_path: Incomplete
    def __init__(self, notify: Notifications, is_allowed_path: Any) -> None: ...
    def send_message(self, message: str, **kwargs: Any) -> None: ...
    def load_file(self, url: Union[str, None] = ..., local_path: Union[str, None] = ..., username: Union[str, None] = ..., password: Union[str, None] = ..., auth: Union[str, None] = ...) -> Union[BufferedReader, bytes, None]: ...

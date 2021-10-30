from .const import ATTR_COLOR as ATTR_COLOR, ATTR_DURATION as ATTR_DURATION, ATTR_FILE as ATTR_FILE, ATTR_FILE_AUTH as ATTR_FILE_AUTH, ATTR_FILE_AUTH_DIGEST as ATTR_FILE_AUTH_DIGEST, ATTR_FILE_PASSWORD as ATTR_FILE_PASSWORD, ATTR_FILE_PATH as ATTR_FILE_PATH, ATTR_FILE_URL as ATTR_FILE_URL, ATTR_FILE_USERNAME as ATTR_FILE_USERNAME, ATTR_FONTSIZE as ATTR_FONTSIZE, ATTR_INTERRUPT as ATTR_INTERRUPT, ATTR_POSITION as ATTR_POSITION, ATTR_TRANSPARENCY as ATTR_TRANSPARENCY, CONF_COLOR as CONF_COLOR, CONF_DURATION as CONF_DURATION, CONF_FONTSIZE as CONF_FONTSIZE, CONF_INTERRUPT as CONF_INTERRUPT, CONF_POSITION as CONF_POSITION, CONF_TRANSPARENCY as CONF_TRANSPARENCY, DEFAULT_TIMEOUT as DEFAULT_TIMEOUT
from homeassistant.components.notify import ATTR_DATA as ATTR_DATA, ATTR_TITLE as ATTR_TITLE, ATTR_TITLE_DEFAULT as ATTR_TITLE_DEFAULT, BaseNotificationService as BaseNotificationService, PLATFORM_SCHEMA as PLATFORM_SCHEMA
from homeassistant.const import ATTR_ICON as ATTR_ICON, CONF_HOST as CONF_HOST, CONF_TIMEOUT as CONF_TIMEOUT
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from notifications_android_tv import Notifications
from typing import Any, BinaryIO

_LOGGER: Any

async def async_get_service(hass: HomeAssistant, config: ConfigType, discovery_info: Union[DiscoveryInfoType, None] = ...) -> NFAndroidTVNotificationService: ...

class NFAndroidTVNotificationService(BaseNotificationService):
    notify: Any
    is_allowed_path: Any
    def __init__(self, notify: Notifications, is_allowed_path: Any) -> None: ...
    def send_message(self, message: str, **kwargs: Any) -> None: ...
    def load_file(self, url: Union[str, None] = ..., local_path: Union[str, None] = ..., username: Union[str, None] = ..., password: Union[str, None] = ..., auth: Union[str, None] = ...) -> Union[bytes, BinaryIO, None]: ...
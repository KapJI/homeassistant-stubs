from aiohttp import BasicAuth
from homeassistant.components.notify import ATTR_DATA as ATTR_DATA, ATTR_TARGET as ATTR_TARGET, ATTR_TITLE as ATTR_TITLE, BaseNotificationService as BaseNotificationService, PLATFORM_SCHEMA as PLATFORM_SCHEMA
from homeassistant.const import ATTR_ICON as ATTR_ICON, CONF_API_KEY as CONF_API_KEY, CONF_ICON as CONF_ICON, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import callback as callback
from homeassistant.helpers import aiohttp_client as aiohttp_client
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType, HomeAssistantType as HomeAssistantType
from slack import WebClient
from typing import Any, TypedDict

ATTR_BLOCKS: str
ATTR_BLOCKS_TEMPLATE: str
ATTR_FILE: str
ATTR_PASSWORD: str
ATTR_PATH: str
ATTR_URL: str
ATTR_USERNAME: str
CONF_DEFAULT_CHANNEL: str
DEFAULT_TIMEOUT_SECONDS: int
FILE_PATH_SCHEMA: Any
FILE_URL_SCHEMA: Any
DATA_FILE_SCHEMA: Any
DATA_TEXT_ONLY_SCHEMA: Any
DATA_SCHEMA: Any

class AuthDictT(TypedDict):
    auth: BasicAuth

class FormDataT(TypedDict):
    channels: str
    filename: str
    initial_comment: str
    title: str
    token: str

class MessageT(TypedDict):
    link_names: bool
    text: str
    username: str
    icon_url: str
    icon_emoji: str
    blocks: list[Any]

async def async_get_service(hass: HomeAssistantType, config: ConfigType, discovery_info: Union[DiscoveryInfoType, None]=...) -> Union[SlackNotificationService, None]: ...

class SlackNotificationService(BaseNotificationService):
    def __init__(self, hass: HomeAssistantType, client: WebClient, default_channel: str, username: Union[str, None], icon: Union[str, None]) -> None: ...
    async def async_send_message(self, message: str, **kwargs: Any) -> None: ...

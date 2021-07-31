from aiohttp import BasicAuth
from homeassistant.components.notify import ATTR_DATA as ATTR_DATA, ATTR_TARGET as ATTR_TARGET, ATTR_TITLE as ATTR_TITLE, BaseNotificationService as BaseNotificationService, PLATFORM_SCHEMA as PLATFORM_SCHEMA
from homeassistant.const import ATTR_ICON as ATTR_ICON, CONF_API_KEY as CONF_API_KEY, CONF_ICON as CONF_ICON, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import aiohttp_client as aiohttp_client, template as template
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from slack import WebClient
from typing import Any, TypedDict

_LOGGER: Any
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

async def async_get_service(hass: HomeAssistant, config: ConfigType, discovery_info: Union[DiscoveryInfoType, None] = ...) -> Union[SlackNotificationService, None]: ...
def _async_get_filename_from_url(url: str) -> str: ...
def _async_sanitize_channel_names(channel_list: list[str]) -> list[str]: ...

class SlackNotificationService(BaseNotificationService):
    _client: Any
    _default_channel: Any
    _hass: Any
    _icon: Any
    _username: Any
    def __init__(self, hass: HomeAssistant, client: WebClient, default_channel: str, username: Union[str, None], icon: Union[str, None]) -> None: ...
    async def _async_send_local_file_message(self, path: str, targets: list[str], message: str, title: Union[str, None]) -> None: ...
    async def _async_send_remote_file_message(self, url: str, targets: list[str], message: str, title: Union[str, None], *, username: Union[str, None] = ..., password: Union[str, None] = ...) -> None: ...
    async def _async_send_text_only_message(self, targets: list[str], message: str, title: Union[str, None], *, username: Union[str, None] = ..., icon: Union[str, None] = ..., blocks: Union[Any, None] = ...) -> None: ...
    async def async_send_message(self, message: str, **kwargs: Any) -> None: ...

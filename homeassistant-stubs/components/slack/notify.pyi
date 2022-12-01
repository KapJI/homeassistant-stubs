from .const import ATTR_BLOCKS as ATTR_BLOCKS, ATTR_BLOCKS_TEMPLATE as ATTR_BLOCKS_TEMPLATE, ATTR_FILE as ATTR_FILE, ATTR_PASSWORD as ATTR_PASSWORD, ATTR_PATH as ATTR_PATH, ATTR_URL as ATTR_URL, ATTR_USERNAME as ATTR_USERNAME, CONF_DEFAULT_CHANNEL as CONF_DEFAULT_CHANNEL, DATA_CLIENT as DATA_CLIENT, SLACK_DATA as SLACK_DATA
from _typeshed import Incomplete
from aiohttp import BasicAuth
from homeassistant.components.notify import ATTR_DATA as ATTR_DATA, ATTR_TARGET as ATTR_TARGET, ATTR_TITLE as ATTR_TITLE, BaseNotificationService as BaseNotificationService, PLATFORM_SCHEMA as PLATFORM_SCHEMA
from homeassistant.const import ATTR_ICON as ATTR_ICON, CONF_API_KEY as CONF_API_KEY, CONF_ICON as CONF_ICON, CONF_PATH as CONF_PATH, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import aiohttp_client as aiohttp_client, template as template
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from slack import WebClient as WebClient
from typing import Any, TypedDict

_LOGGER: Incomplete
FILE_PATH_SCHEMA: Incomplete
FILE_URL_SCHEMA: Incomplete
DATA_FILE_SCHEMA: Incomplete
DATA_TEXT_ONLY_SCHEMA: Incomplete
DATA_SCHEMA: Incomplete

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
    _hass: Incomplete
    _client: Incomplete
    _config: Incomplete
    def __init__(self, hass: HomeAssistant, client: WebClient, config: dict[str, str]) -> None: ...
    async def _async_send_local_file_message(self, path: str, targets: list[str], message: str, title: Union[str, None]) -> None: ...
    async def _async_send_remote_file_message(self, url: str, targets: list[str], message: str, title: Union[str, None], *, username: Union[str, None] = ..., password: Union[str, None] = ...) -> None: ...
    async def _async_send_text_only_message(self, targets: list[str], message: str, title: Union[str, None], *, username: Union[str, None] = ..., icon: Union[str, None] = ..., blocks: Union[Any, None] = ...) -> None: ...
    async def async_send_message(self, message: str, **kwargs: Any) -> None: ...

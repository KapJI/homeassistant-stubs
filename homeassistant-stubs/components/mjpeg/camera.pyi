from .const import CONF_MJPEG_URL as CONF_MJPEG_URL, CONF_STILL_IMAGE_URL as CONF_STILL_IMAGE_URL, DOMAIN as DOMAIN, LOGGER as LOGGER
from aiohttp import web as web
from collections.abc import Iterable
from homeassistant.components.camera import Camera as Camera, PLATFORM_SCHEMA as PLATFORM_SCHEMA
from homeassistant.config_entries import ConfigEntry as ConfigEntry, SOURCE_IMPORT as SOURCE_IMPORT
from homeassistant.const import CONF_AUTHENTICATION as CONF_AUTHENTICATION, CONF_NAME as CONF_NAME, CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME, CONF_VERIFY_SSL as CONF_VERIFY_SSL, HTTP_BASIC_AUTHENTICATION as HTTP_BASIC_AUTHENTICATION, HTTP_DIGEST_AUTHENTICATION as HTTP_DIGEST_AUTHENTICATION
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_aiohttp_proxy_web as async_aiohttp_proxy_web, async_get_clientsession as async_get_clientsession
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

CONTENT_TYPE_HEADER: str
DEFAULT_NAME: str
DEFAULT_VERIFY_SSL: bool

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: Union[DiscoveryInfoType, None] = ...) -> None: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
def extract_image_from_mjpeg(stream: Iterable[bytes]) -> Union[bytes, None]: ...

class MjpegCamera(Camera):
    _attr_name: Any
    _authentication: Any
    _username: Any
    _password: Any
    _mjpeg_url: Any
    _still_image_url: Any
    _auth: Any
    _verify_ssl: Any
    _attr_unique_id: Any
    _attr_device_info: Any
    def __init__(self, *, name: str, mjpeg_url: str, still_image_url: Union[str, None], authentication: Union[str, None] = ..., username: Union[str, None] = ..., password: str = ..., verify_ssl: bool = ..., unique_id: Union[str, None] = ..., device_info: Union[DeviceInfo, None] = ...) -> None: ...
    async def async_camera_image(self, width: Union[int, None] = ..., height: Union[int, None] = ...) -> Union[bytes, None]: ...
    def camera_image(self, width: Union[int, None] = ..., height: Union[int, None] = ...) -> Union[bytes, None]: ...
    async def handle_async_mjpeg_stream(self, request: web.Request) -> Union[web.StreamResponse, None]: ...

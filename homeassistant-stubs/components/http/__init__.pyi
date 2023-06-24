import asyncio
import ssl
from .auth import async_setup_auth as async_setup_auth
from .ban import setup_bans as setup_bans
from .const import KEY_AUTHENTICATED as KEY_AUTHENTICATED, KEY_HASS as KEY_HASS, KEY_HASS_REFRESH_TOKEN_ID as KEY_HASS_REFRESH_TOKEN_ID, KEY_HASS_USER as KEY_HASS_USER
from .cors import setup_cors as setup_cors
from .forwarded import async_setup_forwarded as async_setup_forwarded
from .request_context import current_request as current_request, setup_request_context as setup_request_context
from .security_filter import setup_security_filter as setup_security_filter
from .static import CACHE_HEADERS as CACHE_HEADERS, CachingStaticResource as CachingStaticResource
from .view import HomeAssistantView as HomeAssistantView
from .web_runner import HomeAssistantTCPSite as HomeAssistantTCPSite
from _typeshed import Incomplete
from aiohttp import web
from aiohttp.abc import AbstractStreamWriter as AbstractStreamWriter
from aiohttp.http_parser import RawRequestMessage as RawRequestMessage
from aiohttp.streams import StreamReader as StreamReader
from aiohttp.typedefs import JSONDecoder as JSONDecoder, StrOrURL as StrOrURL
from aiohttp.web_exceptions import HTTPRedirection as HTTPRedirection
from aiohttp.web_log import AccessLogger
from aiohttp.web_protocol import RequestHandler as RequestHandler
from homeassistant.components.network import async_get_source_ip as async_get_source_ip
from homeassistant.const import EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, SERVER_PORT as SERVER_PORT
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import storage as storage
from homeassistant.helpers.network import NoURLAvailableError as NoURLAvailableError, get_url as get_url
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.loader import bind_hass as bind_hass
from homeassistant.setup import async_start_setup as async_start_setup, async_when_setup_or_start as async_when_setup_or_start
from homeassistant.util.json import json_loads as json_loads
from ipaddress import IPv4Network, IPv6Network
from typing import Any, Final, TypedDict

DOMAIN: Final[str]
CONF_SERVER_HOST: Final[str]
CONF_SERVER_PORT: Final[str]
CONF_BASE_URL: Final[str]
CONF_SSL_CERTIFICATE: Final[str]
CONF_SSL_PEER_CERTIFICATE: Final[str]
CONF_SSL_KEY: Final[str]
CONF_CORS_ORIGINS: Final[str]
CONF_USE_X_FORWARDED_FOR: Final[str]
CONF_TRUSTED_PROXIES: Final[str]
CONF_LOGIN_ATTEMPTS_THRESHOLD: Final[str]
CONF_IP_BAN_ENABLED: Final[str]
CONF_SSL_PROFILE: Final[str]
SSL_MODERN: Final[str]
SSL_INTERMEDIATE: Final[str]
_LOGGER: Final[Incomplete]
DEFAULT_DEVELOPMENT: Final[str]
DEFAULT_CORS: Final[list[str]]
NO_LOGIN_ATTEMPT_THRESHOLD: Final[int]
MAX_CLIENT_SIZE: Final[Incomplete]
MAX_LINE_SIZE: Final[int]
STORAGE_KEY: Final[Incomplete]
STORAGE_VERSION: Final[int]
SAVE_DELAY: Final[int]
HTTP_SCHEMA: Final[Incomplete]
CONFIG_SCHEMA: Final[Incomplete]

class ConfData(TypedDict, total=False):
    server_host: list[str]
    server_port: int
    base_url: str
    ssl_certificate: str
    ssl_peer_certificate: str
    ssl_key: str
    cors_allowed_origins: list[str]
    use_x_forwarded_for: bool
    trusted_proxies: list[IPv4Network | IPv6Network]
    login_attempts_threshold: int
    ip_ban_enabled: bool
    ssl_profile: str

async def async_get_last_config(hass: HomeAssistant) -> dict[str, Any] | None: ...

class ApiConfig:
    local_ip: Incomplete
    host: Incomplete
    port: Incomplete
    use_ssl: Incomplete
    def __init__(self, local_ip: str, host: str, port: int, use_ssl: bool) -> None: ...

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...

class HomeAssistantAccessLogger(AccessLogger):
    def log(self, request: web.BaseRequest, response: web.StreamResponse, time: float) -> None: ...

class HomeAssistantRequest(web.Request):
    async def json(self, *, loads: JSONDecoder = ...) -> Any: ...

class HomeAssistantApplication(web.Application):
    def _make_request(self, message: RawRequestMessage, payload: StreamReader, protocol: RequestHandler, writer: AbstractStreamWriter, task: asyncio.Task[None], _cls: type[web.Request] = ...) -> web.Request: ...

class HomeAssistantHTTP:
    app: Incomplete
    hass: Incomplete
    ssl_certificate: Incomplete
    ssl_peer_certificate: Incomplete
    ssl_key: Incomplete
    server_host: Incomplete
    server_port: Incomplete
    trusted_proxies: Incomplete
    ssl_profile: Incomplete
    runner: Incomplete
    site: Incomplete
    context: Incomplete
    def __init__(self, hass: HomeAssistant, ssl_certificate: str | None, ssl_peer_certificate: str | None, ssl_key: str | None, server_host: list[str] | None, server_port: int, trusted_proxies: list[IPv4Network | IPv6Network], ssl_profile: str) -> None: ...
    async def async_initialize(self, *, cors_origins: list[str], use_x_forwarded_for: bool, login_threshold: int, is_ban_enabled: bool) -> None: ...
    def register_view(self, view: HomeAssistantView | type[HomeAssistantView]) -> None: ...
    def register_redirect(self, url: str, redirect_to: StrOrURL, *, redirect_exc: type[HTTPRedirection] = ...) -> None: ...
    def register_static_path(self, url_path: str, path: str, cache_headers: bool = ...) -> None: ...
    def _create_ssl_context(self) -> ssl.SSLContext | None: ...
    def _create_emergency_ssl_context(self) -> ssl.SSLContext: ...
    async def start(self) -> None: ...
    async def stop(self) -> None: ...

async def start_http_server_and_save_config(hass: HomeAssistant, conf: dict, server: HomeAssistantHTTP) -> None: ...

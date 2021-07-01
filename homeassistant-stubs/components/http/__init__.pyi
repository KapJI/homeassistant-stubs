from .auth import setup_auth as setup_auth
from .ban import setup_bans as setup_bans
from .const import KEY_AUTHENTICATED as KEY_AUTHENTICATED, KEY_HASS as KEY_HASS, KEY_HASS_USER as KEY_HASS_USER
from .cors import setup_cors as setup_cors
from .forwarded import async_setup_forwarded as async_setup_forwarded
from .request_context import setup_request_context as setup_request_context
from .security_filter import setup_security_filter as setup_security_filter
from .static import CACHE_HEADERS as CACHE_HEADERS, CachingStaticResource as CachingStaticResource
from .view import HomeAssistantView as HomeAssistantView
from .web_runner import HomeAssistantTCPSite as HomeAssistantTCPSite
from aiohttp import web
from aiohttp.typedefs import StrOrURL as StrOrURL
from aiohttp.web_exceptions import HTTPRedirection as HTTPRedirection
from contextvars import ContextVar
from homeassistant.const import EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, SERVER_PORT as SERVER_PORT
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant
from homeassistant.helpers import storage as storage
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.loader import bind_hass as bind_hass
from homeassistant.setup import async_start_setup as async_start_setup, async_when_setup_or_start as async_when_setup_or_start
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
_LOGGER: Final[Any]
DEFAULT_DEVELOPMENT: Final[str]
DEFAULT_CORS: Final[list[str]]
NO_LOGIN_ATTEMPT_THRESHOLD: Final[int]
MAX_CLIENT_SIZE: Final[Any]
STORAGE_KEY: Final[Any]
STORAGE_VERSION: Final[int]
SAVE_DELAY: Final[int]
HTTP_SCHEMA: Final[Any]
CONFIG_SCHEMA: Final[Any]

class ConfData(TypedDict):
    server_host: list[str]
    server_port: int
    base_url: str
    ssl_certificate: str
    ssl_peer_certificate: str
    ssl_key: str
    cors_allowed_origins: list[str]
    use_x_forwarded_for: bool
    trusted_proxies: list[str]
    login_attempts_threshold: int
    ip_ban_enabled: bool
    ssl_profile: str

async def async_get_last_config(hass: HomeAssistant) -> Union[dict, None]: ...

class ApiConfig:
    local_ip: Any
    host: Any
    port: Any
    use_ssl: Any
    def __init__(self, local_ip: str, host: str, port: int, use_ssl: bool) -> None: ...

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...

class HomeAssistantHTTP:
    hass: Any
    ssl_certificate: Any
    ssl_peer_certificate: Any
    ssl_key: Any
    server_host: Any
    server_port: Any
    trusted_proxies: Any
    is_ban_enabled: Any
    ssl_profile: Any
    _handler: Any
    runner: Any
    site: Any
    def __init__(self, hass: HomeAssistant, ssl_certificate: Union[str, None], ssl_peer_certificate: Union[str, None], ssl_key: Union[str, None], server_host: Union[list[str], None], server_port: int, cors_origins: list[str], use_x_forwarded_for: bool, trusted_proxies: list[str], login_threshold: int, is_ban_enabled: bool, ssl_profile: str) -> None: ...
    def register_view(self, view: HomeAssistantView) -> None: ...
    def register_redirect(self, url: str, redirect_to: StrOrURL, *, redirect_exc: type[HTTPRedirection] = ...) -> None: ...
    def register_static_path(self, url_path: str, path: str, cache_headers: bool = ...) -> Union[web.FileResponse, None]: ...
    async def start(self) -> None: ...
    async def stop(self) -> None: ...

async def start_http_server_and_save_config(hass: HomeAssistant, conf: dict, server: HomeAssistantHTTP) -> None: ...

current_request: ContextVar[Union[web.Request, None]]

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
from contextvars import ContextVar
from homeassistant.const import EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, SERVER_PORT as SERVER_PORT
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant
from homeassistant.helpers import storage as storage
from homeassistant.loader import bind_hass as bind_hass
from homeassistant.setup import async_start_setup as async_start_setup, async_when_setup_or_start as async_when_setup_or_start
from typing import Any

DOMAIN: str
CONF_SERVER_HOST: str
CONF_SERVER_PORT: str
CONF_BASE_URL: str
CONF_SSL_CERTIFICATE: str
CONF_SSL_PEER_CERTIFICATE: str
CONF_SSL_KEY: str
CONF_CORS_ORIGINS: str
CONF_USE_X_FORWARDED_FOR: str
CONF_TRUSTED_PROXIES: str
CONF_LOGIN_ATTEMPTS_THRESHOLD: str
CONF_IP_BAN_ENABLED: str
CONF_SSL_PROFILE: str
SSL_MODERN: str
SSL_INTERMEDIATE: str
_LOGGER: Any
DEFAULT_DEVELOPMENT: str
DEFAULT_CORS: Any
NO_LOGIN_ATTEMPT_THRESHOLD: int
MAX_CLIENT_SIZE: int
STORAGE_KEY = DOMAIN
STORAGE_VERSION: int
HTTP_SCHEMA: Any
CONFIG_SCHEMA: Any

async def async_get_last_config(hass: HomeAssistant) -> Union[dict, None]: ...

class ApiConfig:
    local_ip: Any = ...
    host: Any = ...
    port: Any = ...
    use_ssl: Any = ...
    def __init__(self, local_ip: str, host: str, port: Union[int, None]=..., use_ssl: bool=...) -> None: ...

async def async_setup(hass: Any, config: Any): ...

class HomeAssistantHTTP:
    hass: Any = ...
    ssl_certificate: Any = ...
    ssl_peer_certificate: Any = ...
    ssl_key: Any = ...
    server_host: Any = ...
    server_port: Any = ...
    trusted_proxies: Any = ...
    is_ban_enabled: Any = ...
    ssl_profile: Any = ...
    _handler: Any = ...
    runner: Any = ...
    site: Any = ...
    def __init__(self, hass: Any, ssl_certificate: Any, ssl_peer_certificate: Any, ssl_key: Any, server_host: Any, server_port: Any, cors_origins: Any, use_x_forwarded_for: Any, trusted_proxies: Any, login_threshold: Any, is_ban_enabled: Any, ssl_profile: Any) -> None: ...
    def register_view(self, view: Any) -> None: ...
    def register_redirect(self, url: Any, redirect_to: Any, *, redirect_exc: Any = ...) -> None: ...
    def register_static_path(self, url_path: Any, path: Any, cache_headers: bool = ...): ...
    async def start(self) -> None: ...
    async def stop(self) -> None: ...

async def start_http_server_and_save_config(hass: HomeAssistant, conf: dict, server: HomeAssistantHTTP) -> None: ...

current_request: ContextVar[Union[web.Request, None]]

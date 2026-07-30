import asyncio
import ssl
from .auth import async_setup_auth as async_setup_auth
from .ban import setup_bans as setup_bans
from .config import ConfData as ConfData, _DEFAULT_CONFIG as _DEFAULT_CONFIG, _strip_meta as _strip_meta
from .const import CONF_SERVER_HOST as CONF_SERVER_HOST, CONF_SERVER_PORT as CONF_SERVER_PORT, CONF_SSL_CERTIFICATE as CONF_SSL_CERTIFICATE, CONF_SSL_KEY as CONF_SSL_KEY, CONF_SSL_PEER_CERTIFICATE as CONF_SSL_PEER_CERTIFICATE, CONF_SSL_PROFILE as CONF_SSL_PROFILE, CONF_TRUSTED_PROXIES as CONF_TRUSTED_PROXIES, ENV_SUPERVISOR as ENV_SUPERVISOR, SSL_INTERMEDIATE as SSL_INTERMEDIATE, is_supervisor_unix_socket_request as is_supervisor_unix_socket_request
from .cors import setup_cors as setup_cors
from .forwarded import async_setup_forwarded as async_setup_forwarded
from .headers import setup_headers as setup_headers
from .request_context import setup_request_context as setup_request_context
from .security_filter import setup_security_filter as setup_security_filter
from .static import CACHE_HEADERS as CACHE_HEADERS, CachingStaticResource as CachingStaticResource
from .web_runner import HomeAssistantUnixSite as HomeAssistantUnixSite
from _typeshed import Incomplete
from aiohttp import web
from aiohttp.abc import AbstractStreamWriter as AbstractStreamWriter
from aiohttp.http_parser import RawRequestMessage as RawRequestMessage
from aiohttp.streams import StreamReader as StreamReader
from aiohttp.typedefs import JSONDecoder as JSONDecoder, StrOrURL as StrOrURL
from aiohttp.web_exceptions import HTTPRedirection as HTTPRedirection
from aiohttp.web_protocol import RequestHandler as RequestHandler
from collections.abc import Collection
from dataclasses import dataclass
from homeassistant.const import SERVER_PORT as SERVER_PORT
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.http import HomeAssistantView as HomeAssistantView, KEY_ALLOW_CONFIGURED_CORS as KEY_ALLOW_CONFIGURED_CORS, KEY_HASS as KEY_HASS, current_request as current_request
from homeassistant.helpers.network import NoURLAvailableError as NoURLAvailableError, get_url as get_url
from homeassistant.setup import async_when_setup as async_when_setup
from homeassistant.util.json import json_loads as json_loads
from ipaddress import IPv4Network, IPv6Network
from pathlib import Path
from typing import Any, Final, override

_LOGGER: Final[Incomplete]
MAX_CLIENT_SIZE: Final[Incomplete]
MAX_LINE_SIZE: Final[int]
_HAS_IPV6: Incomplete
DEFAULT_BIND: Incomplete

@dataclass(slots=True)
class StaticPathConfig:
    url_path: str
    path: str
    cache_headers: bool = ...

_STATIC_CLASSES: Incomplete

def make_server(hass: HomeAssistant, conf: ConfData, supervisor_unix_socket_path: Path | None = None) -> HomeAssistantHTTP: ...
async def async_verify_can_bind(hass: HomeAssistant, conf: ConfData) -> None: ...

class HomeAssistantRequest(web.Request):
    @override
    async def json(self, *, loads: JSONDecoder = ...) -> Any: ...

class HomeAssistantApplication(web.Application):
    @override
    def _make_request(self, message: RawRequestMessage, payload: StreamReader, protocol: RequestHandler, writer: AbstractStreamWriter, task: asyncio.Task[None], _cls: type[web.Request] = ...) -> web.Request: ...

async def _serve_file_with_cache_headers(path: str, request: web.Request) -> web.FileResponse: ...
async def _serve_file(path: str, request: web.Request) -> web.FileResponse: ...

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
    supervisor_unix_socket_path: Incomplete
    runner: web.AppRunner | None
    supervisor_site: HomeAssistantUnixSite | None
    context: ssl.SSLContext | None
    _server: asyncio.Server | None
    _port_transition: Incomplete
    _legacy_redirect_runner: web.AppRunner | None
    _legacy_redirect_server: asyncio.Server | None
    def __init__(self, hass: HomeAssistant, ssl_certificate: str | None, ssl_peer_certificate: str | None, ssl_key: str | None, server_host: list[str] | None, server_port: int, trusted_proxies: list[IPv4Network | IPv6Network], ssl_profile: str, supervisor_unix_socket_path: Path | None = None, port_transition: bool = False) -> None: ...
    async def async_bind(self) -> None: ...
    async def _async_create_server(self) -> asyncio.Server: ...
    def _make_protocol(self) -> RequestHandler: ...
    async def async_initialize(self, *, cors_origins: list[str], use_x_forwarded_for: bool, login_threshold: int, is_ban_enabled: bool, use_x_frame_options: bool) -> None: ...
    def register_view(self, view: HomeAssistantView | type[HomeAssistantView]) -> None: ...
    def register_redirect(self, url: str, redirect_to: StrOrURL, *, redirect_exc: type[HTTPRedirection] = ...) -> None: ...
    def _make_static_resources(self, configs: Collection[StaticPathConfig]) -> dict[str, CachingStaticResource | web.StaticResource | None]: ...
    async def async_register_static_paths(self, configs: Collection[StaticPathConfig]) -> None: ...
    @callback
    def _async_register_static_paths(self, configs: Collection[StaticPathConfig], resources: dict[str, CachingStaticResource | web.StaticResource | None]) -> None: ...
    def _create_ssl_context(self) -> ssl.SSLContext | None: ...
    def _create_emergency_ssl_context(self) -> ssl.SSLContext: ...
    async def async_start_supervisor_unix_socket(self) -> None: ...
    async def start(self) -> None: ...
    async def _async_manage_port_transition(self, hass: HomeAssistant, _component: str) -> None: ...
    @callback
    def _on_onboarding_complete(self) -> None: ...
    async def _async_start_legacy_redirect(self) -> None: ...
    async def _async_create_redirect_server(self) -> asyncio.Server: ...
    async def _async_stop_legacy_redirect(self) -> None: ...
    async def stop(self) -> None: ...

class HassioHTTPConfigView(HomeAssistantView):
    url: str
    name: str
    @callback
    def get(self, request: web.Request) -> web.Response: ...

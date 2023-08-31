from .view import HomeAssistantView as HomeAssistantView
from _typeshed import Incomplete
from aiohttp.web import Application as Application, Request as Request, Response as Response, StreamResponse as StreamResponse
from collections.abc import Awaitable, Callable as Callable, Coroutine
from datetime import datetime
from homeassistant.components import persistent_notification as persistent_notification
from homeassistant.config import load_yaml_config_file as load_yaml_config_file
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.util import yaml as yaml
from ipaddress import IPv4Address, IPv6Address
from typing import Any, Concatenate, Final, TypeVar

_HassViewT = TypeVar('_HassViewT', bound=HomeAssistantView)
_P: Incomplete
_LOGGER: Final[Incomplete]
KEY_BAN_MANAGER: Final[str]
KEY_FAILED_LOGIN_ATTEMPTS: Final[str]
KEY_LOGIN_THRESHOLD: Final[str]
NOTIFICATION_ID_BAN: Final[str]
NOTIFICATION_ID_LOGIN: Final[str]
IP_BANS_FILE: Final[str]
ATTR_BANNED_AT: Final[str]
SCHEMA_IP_BAN_ENTRY: Final[Incomplete]

def setup_bans(hass: HomeAssistant, app: Application, login_threshold: int) -> None: ...
async def ban_middleware(request: Request, handler: Callable[[Request], Awaitable[StreamResponse]]) -> StreamResponse: ...
def log_invalid_auth(func: Callable[Concatenate[_HassViewT, Request, _P], Awaitable[Response]]) -> Callable[Concatenate[_HassViewT, Request, _P], Coroutine[Any, Any, Response]]: ...
async def process_wrong_login(request: Request) -> None: ...
async def process_success_login(request: Request) -> None: ...

class IpBan:
    ip_address: Incomplete
    banned_at: Incomplete
    def __init__(self, ip_ban: str | IPv4Address | IPv6Address, banned_at: datetime | None = ...) -> None: ...

class IpBanManager:
    hass: Incomplete
    path: Incomplete
    ip_bans_lookup: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    async def async_load(self) -> None: ...
    def _add_ban(self, ip_ban: IpBan) -> None: ...
    async def async_add_ban(self, remote_addr: IPv4Address | IPv6Address) -> None: ...

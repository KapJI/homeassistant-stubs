from . import AuthManager as AuthManager
from .models import RefreshToken as RefreshToken
from _typeshed import Incomplete
from aiohttp.web import Request as Request
from aiohttp_session import Session as Session
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.event import async_call_later as async_call_later
from homeassistant.helpers.storage import Store as Store
from typing import TypedDict

TEMP_TIMEOUT: Incomplete
TEMP_TIMEOUT_SECONDS: Incomplete
SESSION_ID: str
STORAGE_VERSION: int
STORAGE_KEY: str

class StrictConnectionTempSessionData:
    __slots__: Incomplete
    cancel_remove: Incomplete
    absolute_expiry: Incomplete
    def __init__(self, cancel_remove: CALLBACK_TYPE) -> None: ...

class StoreData(TypedDict):
    unauthorized_sessions: dict[str, str]
    key: str

class SessionManager:
    _auth: Incomplete
    _hass: Incomplete
    _temp_sessions: Incomplete
    _strict_connection_sessions: Incomplete
    _store: Incomplete
    _key: Incomplete
    _refresh_token_revoke_callbacks: Incomplete
    def __init__(self, hass: HomeAssistant, auth: AuthManager) -> None: ...
    @property
    def key(self) -> str: ...
    async def async_validate_request_for_strict_connection_session(self, request: Request) -> bool: ...
    def async_validate_strict_connection_session(self, session: Session) -> bool: ...
    def _async_register_revoke_token_callback(self, refresh_token_id: str) -> None: ...
    async def async_create_session(self, request: Request, refresh_token: RefreshToken) -> None: ...
    async def async_create_temp_unauthorized_session(self, request: Request) -> None: ...
    async def _async_create_new_session(self, request: Request, *, max_age: int | None = None) -> str: ...
    def _async_schedule_save(self, delay: float = 1) -> None: ...
    def _data_to_save(self) -> StoreData: ...
    async def async_setup(self) -> None: ...

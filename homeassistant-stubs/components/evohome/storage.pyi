from .const import STORAGE_KEY as STORAGE_KEY, STORAGE_VER as STORAGE_VER
from _typeshed import Incomplete
from evohomeasync.auth import AbstractSessionManager
from evohomeasync2.auth import AbstractTokenManager
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.storage import Store as Store
from typing import Any, NotRequired, TypedDict

class _SessionIdEntryT(TypedDict):
    session_id: str
    session_id_expires: NotRequired[str]

class _TokenStoreT(TypedDict):
    username: str
    refresh_token: str
    access_token: str
    access_token_expires: str
    session_id: NotRequired[str]
    session_id_expires: NotRequired[str]

class TokenManager(AbstractTokenManager, AbstractSessionManager):
    _store: Incomplete
    _store_initialized: bool
    def __init__(self, hass: HomeAssistant, *args: Any, **kwargs: Any) -> None: ...
    async def get_access_token(self) -> str: ...
    async def get_session_id(self) -> str: ...
    async def _load_cache_from_store(self) -> None: ...
    _session_id: Incomplete
    _session_id_expires: Incomplete
    def _import_session_id(self, session: _SessionIdEntryT) -> None: ...
    async def save_access_token(self) -> None: ...
    async def save_session_id(self) -> None: ...
    async def save_cache_to_store(self) -> None: ...

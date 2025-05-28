from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from homeassistant.components import websocket_api as websocket_api
from homeassistant.components.websocket_api import ActiveConnection as ActiveConnection
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.storage import Store as Store
from homeassistant.util.hass_dict import HassKey as HassKey
from typing import Any

DATA_STORAGE: HassKey[dict[str, UserStore]]
STORAGE_VERSION_USER_DATA: int

async def async_setup_frontend_storage(hass: HomeAssistant) -> None: ...
async def async_user_store(hass: HomeAssistant, user_id: str) -> UserStore: ...

class UserStore:
    _store: Incomplete
    data: dict[str, Any]
    subscriptions: dict[str | None, list[Callable[[], None]]]
    def __init__(self, hass: HomeAssistant, user_id: str) -> None: ...
    async def async_load(self) -> None: ...
    async def async_set_item(self, key: str, value: Any) -> None: ...
    @callback
    def async_subscribe(self, key: str | None, on_update_callback: Callable[[], None]) -> Callable[[], None]: ...

class _UserStore(Store[dict[str, Any]]):
    def __init__(self, hass: HomeAssistant, user_id: str) -> None: ...

def with_user_store(orig_func: Callable[[HomeAssistant, ActiveConnection, dict[str, Any], UserStore], Coroutine[Any, Any, None]]) -> Callable[[HomeAssistant, ActiveConnection, dict[str, Any]], Coroutine[Any, Any, None]]: ...
@websocket_api.async_response
@with_user_store
async def websocket_set_user_data(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any], store: UserStore) -> None: ...
@websocket_api.async_response
@with_user_store
async def websocket_get_user_data(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any], store: UserStore) -> None: ...
@websocket_api.async_response
@with_user_store
async def websocket_subscribe_user_data(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any], store: UserStore) -> None: ...

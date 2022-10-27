from collections.abc import Callable as Callable
from homeassistant.components import websocket_api as websocket_api
from homeassistant.components.websocket_api.connection import ActiveConnection as ActiveConnection
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.storage import Store as Store
from typing import Any

DATA_STORAGE: str
STORAGE_VERSION_USER_DATA: int

async def async_setup_frontend_storage(hass: HomeAssistant) -> None: ...
def with_store(orig_func: Callable) -> Callable: ...
async def websocket_set_user_data(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any], store: Store, data: dict[str, Any]) -> None: ...
async def websocket_get_user_data(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any], store: Store, data: dict[str, Any]) -> None: ...

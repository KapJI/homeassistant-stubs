from homeassistant.components import websocket_api as websocket_api
from typing import Any

DATA_STORAGE: str
STORAGE_VERSION_USER_DATA: int

async def async_setup_frontend_storage(hass: Any) -> None: ...
def with_store(orig_func: Any): ...
async def websocket_set_user_data(hass: Any, connection: Any, msg: Any, store: Any, data: Any) -> None: ...
async def websocket_get_user_data(hass: Any, connection: Any, msg: Any, store: Any, data: Any) -> None: ...
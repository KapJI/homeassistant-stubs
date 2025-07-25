from .const import ATTR_REVERSE as ATTR_REVERSE, DEFAULT_REVERSE as DEFAULT_REVERSE, DOMAIN as DOMAIN, EVENT_SHOPPING_LIST_UPDATED as EVENT_SHOPPING_LIST_UPDATED, SERVICE_ADD_ITEM as SERVICE_ADD_ITEM, SERVICE_CLEAR_COMPLETED_ITEMS as SERVICE_CLEAR_COMPLETED_ITEMS, SERVICE_COMPLETE_ALL as SERVICE_COMPLETE_ALL, SERVICE_COMPLETE_ITEM as SERVICE_COMPLETE_ITEM, SERVICE_INCOMPLETE_ALL as SERVICE_INCOMPLETE_ALL, SERVICE_INCOMPLETE_ITEM as SERVICE_INCOMPLETE_ITEM, SERVICE_REMOVE_ITEM as SERVICE_REMOVE_ITEM, SERVICE_SORT as SERVICE_SORT
from _typeshed import Incomplete
from aiohttp import web as web
from collections.abc import Callable as Callable
from homeassistant import config_entries as config_entries
from homeassistant.components import http as http, websocket_api as websocket_api
from homeassistant.components.http.data_validator import RequestDataValidator as RequestDataValidator
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_NAME as ATTR_NAME, Platform as Platform
from homeassistant.core import Context as Context, HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.helpers.json import save_json as save_json
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.util.json import JsonValueType as JsonValueType, load_json_array as load_json_array
from typing import Any

PLATFORMS: Incomplete
ATTR_COMPLETE: str
_LOGGER: Incomplete
CONFIG_SCHEMA: Incomplete
ITEM_UPDATE_SCHEMA: Incomplete
PERSISTENCE: str
SERVICE_ITEM_SCHEMA: Incomplete
SERVICE_LIST_SCHEMA: Incomplete
SERVICE_SORT_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool: ...

class NoMatchingShoppingListItem(Exception): ...

class ShoppingData:
    hass: Incomplete
    items: list[dict[str, JsonValueType]]
    _listeners: list[Callable[[], None]]
    def __init__(self, hass: HomeAssistant) -> None: ...
    async def async_add(self, name: str | None, complete: bool = False, context: Context | None = None) -> dict[str, JsonValueType]: ...
    async def async_remove(self, item_id: str, context: Context | None = None) -> dict[str, JsonValueType] | None: ...
    async def async_remove_items(self, item_ids: set[str], context: Context | None = None) -> list[dict[str, JsonValueType]]: ...
    async def async_complete(self, name: str, context: Context | None = None) -> list[dict[str, JsonValueType]]: ...
    async def async_update(self, item_id: str | None, info: dict[str, Any], context: Context | None = None) -> dict[str, JsonValueType]: ...
    async def async_clear_completed(self, context: Context | None = None) -> None: ...
    async def async_update_list(self, info: dict[str, JsonValueType], context: Context | None = None) -> list[dict[str, JsonValueType]]: ...
    @callback
    def async_reorder(self, item_ids: list[str], context: Context | None = None) -> None: ...
    async def async_move_item(self, uid: str, previous: str | None = None) -> None: ...
    async def async_sort(self, reverse: bool = False, context: Context | None = None) -> None: ...
    async def async_load(self) -> None: ...
    def save(self) -> None: ...
    def async_add_listener(self, cb: Callable[[], None]) -> Callable[[], None]: ...
    def _async_notify(self) -> None: ...

class ShoppingListView(http.HomeAssistantView):
    url: str
    name: str
    @callback
    def get(self, request: web.Request) -> web.Response: ...

class UpdateShoppingListItemView(http.HomeAssistantView):
    url: str
    name: str
    async def post(self, request: web.Request, item_id: str) -> web.Response: ...

class CreateShoppingListItemView(http.HomeAssistantView):
    url: str
    name: str
    async def post(self, request: web.Request, data: dict[str, str]) -> web.Response: ...

class ClearCompletedItemsView(http.HomeAssistantView):
    url: str
    name: str
    async def post(self, request: web.Request) -> web.Response: ...

@callback
def websocket_handle_items(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@websocket_api.async_response
async def websocket_handle_add(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@websocket_api.async_response
async def websocket_handle_remove(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@websocket_api.async_response
async def websocket_handle_update(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@websocket_api.async_response
async def websocket_handle_clear(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
def websocket_handle_reorder(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...

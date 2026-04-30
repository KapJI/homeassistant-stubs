from .common import NoMatchingShoppingListItem as NoMatchingShoppingListItem, ShoppingData as ShoppingData, ShoppingListConfigEntry as ShoppingListConfigEntry, _get_shopping_data as _get_shopping_data
from .const import ATTR_REVERSE as ATTR_REVERSE, DEFAULT_REVERSE as DEFAULT_REVERSE, DOMAIN as DOMAIN, SERVICE_ADD_ITEM as SERVICE_ADD_ITEM, SERVICE_CLEAR_COMPLETED_ITEMS as SERVICE_CLEAR_COMPLETED_ITEMS, SERVICE_COMPLETE_ALL as SERVICE_COMPLETE_ALL, SERVICE_COMPLETE_ITEM as SERVICE_COMPLETE_ITEM, SERVICE_INCOMPLETE_ALL as SERVICE_INCOMPLETE_ALL, SERVICE_INCOMPLETE_ITEM as SERVICE_INCOMPLETE_ITEM, SERVICE_REMOVE_ITEM as SERVICE_REMOVE_ITEM, SERVICE_SORT as SERVICE_SORT
from _typeshed import Incomplete
from aiohttp import web as web
from homeassistant import config_entries as config_entries
from homeassistant.components import http as http, websocket_api as websocket_api
from homeassistant.components.http.data_validator import RequestDataValidator as RequestDataValidator
from homeassistant.const import ATTR_NAME as ATTR_NAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any

PLATFORMS: Incomplete
_LOGGER: Incomplete
CONFIG_SCHEMA: Incomplete
SERVICE_ITEM_SCHEMA: Incomplete
SERVICE_LIST_SCHEMA: Incomplete
SERVICE_SORT_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def _async_setup(hass: HomeAssistant) -> None: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ShoppingListConfigEntry) -> bool: ...

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
@websocket_api.async_response
async def websocket_handle_reorder(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...

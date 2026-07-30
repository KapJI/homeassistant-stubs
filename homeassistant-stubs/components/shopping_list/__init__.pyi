from .common import NoMatchingShoppingListItem as NoMatchingShoppingListItem, ShoppingData as ShoppingData, ShoppingListConfigEntry as ShoppingListConfigEntry, _get_shopping_data as _get_shopping_data
from .const import DOMAIN as DOMAIN
from .services import async_register_services as async_register_services
from _typeshed import Incomplete
from aiohttp import web as web
from homeassistant import config_entries as config_entries
from homeassistant.components import http as http, websocket_api as websocket_api
from homeassistant.components.http.data_validator import RequestDataValidator as RequestDataValidator
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any

PLATFORMS: Incomplete
_LOGGER: Incomplete
CONFIG_SCHEMA: Incomplete

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

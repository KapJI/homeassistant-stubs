from .const import ATTR_DESCRIPTION as ATTR_DESCRIPTION, ATTR_DUE as ATTR_DUE, ATTR_DUE_DATE as ATTR_DUE_DATE, ATTR_DUE_DATETIME as ATTR_DUE_DATETIME, ATTR_ITEM as ATTR_ITEM, ATTR_RENAME as ATTR_RENAME, ATTR_STATUS as ATTR_STATUS, DATA_COMPONENT as DATA_COMPONENT, DOMAIN as DOMAIN, TodoItemStatus as TodoItemStatus, TodoListEntityFeature as TodoListEntityFeature, TodoServices as TodoServices
from .entity import TodoItem as TodoItem, TodoListEntity as TodoListEntity, api_items_factory as api_items_factory, serialize_todo_item as serialize_todo_item
from .services import async_setup_services as async_setup_services
from _typeshed import Incomplete
from homeassistant.components import frontend as frontend, websocket_api as websocket_api
from homeassistant.components.websocket_api import ERR_NOT_FOUND as ERR_NOT_FOUND, ERR_NOT_SUPPORTED as ERR_NOT_SUPPORTED
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_ENTITY_ID as CONF_ENTITY_ID
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any

_LOGGER: Incomplete
ENTITY_ID_FORMAT: Incomplete
PLATFORM_SCHEMA: Incomplete
PLATFORM_SCHEMA_BASE: Incomplete
SCAN_INTERVAL: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
@websocket_api.async_response
async def websocket_handle_subscribe_todo_items(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@websocket_api.async_response
async def websocket_handle_todo_item_list(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@websocket_api.async_response
async def websocket_handle_todo_item_move(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...

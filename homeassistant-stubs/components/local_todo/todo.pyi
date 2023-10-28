from .const import CONF_TODO_LIST_NAME as CONF_TODO_LIST_NAME, DOMAIN as DOMAIN
from .store import LocalTodoListStore as LocalTodoListStore
from _typeshed import Incomplete
from collections.abc import Iterable
from homeassistant.components.todo import TodoItem as TodoItem, TodoItemStatus as TodoItemStatus, TodoListEntity as TodoListEntity, TodoListEntityFeature as TodoListEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from ical.calendar import Calendar as Calendar
from ical.todo import Todo
from typing import Any

_LOGGER: Incomplete
PRODID: str
ICS_TODO_STATUS_MAP: Incomplete
ICS_TODO_STATUS_MAP_INV: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
def _todo_dict_factory(obj: Iterable[tuple[str, Any]]) -> dict[str, str]: ...
def _convert_item(item: TodoItem) -> Todo: ...

class LocalTodoListEntity(TodoListEntity):
    _attr_has_entity_name: bool
    _attr_supported_features: Incomplete
    _attr_should_poll: bool
    _store: Incomplete
    _calendar: Incomplete
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, store: LocalTodoListStore, calendar: Calendar, name: str, unique_id: str) -> None: ...
    _attr_todo_items: Incomplete
    async def async_update(self) -> None: ...
    async def async_create_todo_item(self, item: TodoItem) -> None: ...
    async def async_update_todo_item(self, item: TodoItem) -> None: ...
    async def async_delete_todo_items(self, uids: list[str]) -> None: ...
    async def async_move_todo_item(self, uid: str, previous_uid: str | None = ...) -> None: ...
    async def _async_save(self) -> None: ...

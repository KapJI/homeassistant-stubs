from . import NoMatchingShoppingListItem as NoMatchingShoppingListItem, ShoppingData as ShoppingData
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.todo import TodoItem as TodoItem, TodoItemStatus as TodoItemStatus, TodoListEntity as TodoListEntity, TodoListEntityFeature as TodoListEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ShoppingTodoListEntity(TodoListEntity):
    _attr_has_entity_name: bool
    _attr_icon: str
    _attr_translation_key: str
    _attr_should_poll: bool
    _attr_supported_features: Incomplete
    _attr_unique_id: Incomplete
    _data: Incomplete
    def __init__(self, data: ShoppingData, unique_id: str) -> None: ...
    async def async_create_todo_item(self, item: TodoItem) -> None: ...
    async def async_update_todo_item(self, item: TodoItem) -> None: ...
    async def async_delete_todo_items(self, uids: list[str]) -> None: ...
    async def async_move_todo_item(self, uid: str, previous_uid: str | None = None) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @property
    def todo_items(self) -> list[TodoItem]: ...

from .const import CONF_LIST_ID as CONF_LIST_ID, DOMAIN as DOMAIN, SUBENTRY_TYPE_LIST as SUBENTRY_TYPE_LIST
from .coordinator import RememberTheMilkConfigEntry as RememberTheMilkConfigEntry, RtmTodoCoordinator as RtmTodoCoordinator
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable, Coroutine
from homeassistant.components.todo import TodoItem as TodoItem, TodoItemStatus as TodoItemStatus, TodoListEntity as TodoListEntity, TodoListEntityFeature as TodoListEntityFeature
from homeassistant.config_entries import ConfigSubentry as ConfigSubentry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any, override

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: RememberTheMilkConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...
def handle_api_errors[**_P](func: Callable[_P, Awaitable[None]]) -> Callable[_P, Coroutine[Any, Any, None]]: ...

class RtmTodoListEntity(CoordinatorEntity[RtmTodoCoordinator], TodoListEntity):
    _attr_has_entity_name: bool
    _attr_name: Incomplete
    _attr_supported_features: Incomplete
    _list_id: int
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: RtmTodoCoordinator, subentry: ConfigSubentry) -> None: ...
    @property
    @override
    def todo_items(self) -> list[TodoItem]: ...
    @handle_api_errors
    @override
    async def async_create_todo_item(self, item: TodoItem) -> None: ...
    @handle_api_errors
    @override
    async def async_update_todo_item(self, item: TodoItem) -> None: ...
    @handle_api_errors
    @override
    async def async_delete_todo_items(self, uids: list[str]) -> None: ...

def _parse_uid(uid: str) -> tuple[int, int, int]: ...

from .const import DOMAIN as DOMAIN
from .coordinator import BringConfigEntry as BringConfigEntry, BringData as BringData, BringDataUpdateCoordinator as BringDataUpdateCoordinator
from .entity import BringBaseEntity as BringBaseEntity
from _typeshed import Incomplete
from bring_api import BringList as BringList, BringNotificationType as BringNotificationType
from homeassistant.components.todo import TodoItem as TodoItem, TodoItemStatus as TodoItemStatus, TodoListEntity as TodoListEntity, TodoListEntityFeature as TodoListEntityFeature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, ServiceValidationError as ServiceValidationError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, config_entry: BringConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class BringTodoListEntity(BringBaseEntity, TodoListEntity):
    _attr_translation_key: str
    _attr_name: Incomplete
    _attr_supported_features: Incomplete
    coordinator: BringDataUpdateCoordinator
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: BringDataUpdateCoordinator, bring_list: BringList) -> None: ...
    @property
    def todo_items(self) -> list[TodoItem]: ...
    @property
    def bring_list(self) -> BringData: ...
    async def async_create_todo_item(self, item: TodoItem) -> None: ...
    async def async_update_todo_item(self, item: TodoItem) -> None: ...
    async def async_delete_todo_items(self, uids: list[str]) -> None: ...
    async def async_send_message(self, message: BringNotificationType, item: str | None = None) -> None: ...

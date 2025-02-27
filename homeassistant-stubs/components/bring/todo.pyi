from .const import ATTR_ITEM_NAME as ATTR_ITEM_NAME, ATTR_NOTIFICATION_TYPE as ATTR_NOTIFICATION_TYPE, DOMAIN as DOMAIN, SERVICE_PUSH_NOTIFICATION as SERVICE_PUSH_NOTIFICATION
from .coordinator import BringConfigEntry as BringConfigEntry, BringData as BringData, BringDataUpdateCoordinator as BringDataUpdateCoordinator
from .entity import BringBaseEntity as BringBaseEntity
from _typeshed import Incomplete
from bring_api import BringList as BringList, BringNotificationType
from homeassistant.components.todo import TodoItem as TodoItem, TodoItemStatus as TodoItemStatus, TodoListEntity as TodoListEntity, TodoListEntityFeature as TodoListEntityFeature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, ServiceValidationError as ServiceValidationError
from homeassistant.helpers import entity_platform as entity_platform
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, config_entry: BringConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class BringTodoListEntity(BringBaseEntity, TodoListEntity):
    _attr_translation_key: str
    _attr_name: Incomplete
    _attr_supported_features: Incomplete
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

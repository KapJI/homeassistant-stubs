from .const import ASSETS_URL as ASSETS_URL, DOMAIN as DOMAIN
from .coordinator import HabiticaConfigEntry as HabiticaConfigEntry, HabiticaDataUpdateCoordinator as HabiticaDataUpdateCoordinator
from .entity import HabiticaBase as HabiticaBase
from .util import next_due_date as next_due_date
from _typeshed import Incomplete
from enum import StrEnum
from homeassistant.components import persistent_notification as persistent_notification
from homeassistant.components.todo import TodoItem as TodoItem, TodoItemStatus as TodoItemStatus, TodoListEntity as TodoListEntity, TodoListEntityFeature as TodoListEntityFeature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, ServiceValidationError as ServiceValidationError
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

_LOGGER: Incomplete
PARALLEL_UPDATES: int

class HabiticaTodoList(StrEnum):
    HABITS = 'habits'
    DAILIES = 'dailys'
    TODOS = 'todos'
    REWARDS = 'rewards'

async def async_setup_entry(hass: HomeAssistant, config_entry: HabiticaConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class BaseHabiticaListEntity(HabiticaBase, TodoListEntity):
    def __init__(self, coordinator: HabiticaDataUpdateCoordinator) -> None: ...
    async def async_delete_todo_items(self, uids: list[str]) -> None: ...
    async def async_move_todo_item(self, uid: str, previous_uid: str | None = None) -> None: ...
    async def async_update_todo_item(self, item: TodoItem) -> None: ...

class HabiticaTodosListEntity(BaseHabiticaListEntity):
    _attr_supported_features: Incomplete
    entity_description: Incomplete
    @property
    def todo_items(self) -> list[TodoItem]: ...
    async def async_create_todo_item(self, item: TodoItem) -> None: ...

class HabiticaDailiesListEntity(BaseHabiticaListEntity):
    _attr_supported_features: Incomplete
    entity_description: Incomplete
    @property
    def todo_items(self) -> list[TodoItem]: ...

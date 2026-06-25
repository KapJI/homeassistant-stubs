from .const import _LOGGER as _LOGGER
from .coordinator import AmazonConfigEntry as AmazonConfigEntry, AmazonDevicesCoordinator as AmazonDevicesCoordinator, alexa_api_call as alexa_api_call
from .entity import AmazonServiceEntity as AmazonServiceEntity
from _typeshed import Incomplete
from aioamazondevices.structures import AmazonListInfo as AmazonListInfo
from homeassistant.components.todo import TodoItem as TodoItem, TodoItemStatus as TodoItemStatus, TodoListEntity as TodoListEntity, TodoListEntityFeature as TodoListEntityFeature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import override

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: AmazonConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class AlexaToDoList(AmazonServiceEntity, TodoListEntity):
    _attr_supported_features: Incomplete
    _list: Incomplete
    def __init__(self, coordinator: AmazonDevicesCoordinator, alexa_list: AmazonListInfo) -> None: ...
    @property
    @override
    def todo_items(self) -> list[TodoItem]: ...
    @override
    async def async_create_todo_item(self, item: TodoItem) -> None: ...
    @override
    async def async_delete_todo_items(self, uids: list[str]) -> None: ...
    @override
    async def async_update_todo_item(self, item: TodoItem) -> None: ...

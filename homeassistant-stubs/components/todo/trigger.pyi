import abc
import asyncio
from . import TodoItem as TodoItem, TodoListEntity as TodoListEntity
from .const import DATA_COMPONENT as DATA_COMPONENT, DOMAIN as DOMAIN, TodoItemStatus as TodoItemStatus
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, CONF_TARGET as CONF_TARGET
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant, callback as callback, split_entity_id as split_entity_id
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.target import TargetEntityChangeTracker as TargetEntityChangeTracker, TargetSelection as TargetSelection
from homeassistant.helpers.trigger import Trigger as Trigger, TriggerActionRunner as TriggerActionRunner, TriggerConfig as TriggerConfig
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import override

ITEM_TRIGGER_SCHEMA: Incomplete
_LOGGER: Incomplete

def get_entity(hass: HomeAssistant, entity_id: str) -> TodoListEntity: ...

@dataclass(frozen=True, slots=True)
class TodoItemChangeEvent:
    entity_id: str
    items: list[TodoItem] | None

class ItemChangeListener(TargetEntityChangeTracker):
    _listener: Incomplete
    _entities_updated: Incomplete
    _pending_listener_task: asyncio.Task[None] | None
    _unsubscribe_listeners: list[CALLBACK_TYPE]
    def __init__(self, hass: HomeAssistant, target_selection: TargetSelection, listener: Callable[[TodoItemChangeEvent], None], entities_updated: Callable[[set[str]], None]) -> None: ...
    @override
    @callback
    def _handle_entities_update(self, tracked_entities: set[str]) -> None: ...
    async def _start_listening(self, tracked_entities: set[str]) -> None: ...
    @override
    @callback
    def _unsubscribe(self) -> None: ...

class ItemTriggerBase(Trigger, abc.ABC, metaclass=abc.ABCMeta):
    @classmethod
    async def async_validate_config(cls, hass: HomeAssistant, config: ConfigType) -> ConfigType: ...
    _target: Incomplete
    def __init__(self, hass: HomeAssistant, config: TriggerConfig) -> None: ...
    async def async_attach_runner(self, run_action: TriggerActionRunner) -> CALLBACK_TYPE: ...
    @callback
    @abc.abstractmethod
    def _handle_item_change(self, event: TodoItemChangeEvent, run_action: TriggerActionRunner) -> None: ...
    @callback
    @abc.abstractmethod
    def _handle_entities_updated(self, tracked_entities: set[str]) -> None: ...

class ItemChangeTriggerBase(ItemTriggerBase, metaclass=abc.ABCMeta):
    _entity_item_ids: dict[str, set[str] | None]
    _description: Incomplete
    def __init__(self, hass: HomeAssistant, config: TriggerConfig, description: str) -> None: ...
    @abc.abstractmethod
    def _is_matching_item(self, item: TodoItem) -> bool: ...
    @abc.abstractmethod
    def _get_items_diff(self, old_item_ids: set[str], current_item_ids: set[str]) -> set[str]: ...
    @override
    @callback
    def _handle_item_change(self, event: TodoItemChangeEvent, run_action: TriggerActionRunner) -> None: ...
    @override
    @callback
    def _handle_entities_updated(self, tracked_entities: set[str]) -> None: ...

class ItemAddedTrigger(ItemChangeTriggerBase):
    def __init__(self, hass: HomeAssistant, config: TriggerConfig) -> None: ...
    @override
    def _is_matching_item(self, item: TodoItem) -> bool: ...
    @override
    def _get_items_diff(self, old_item_ids: set[str], current_item_ids: set[str]) -> set[str]: ...

class ItemRemovedTrigger(ItemChangeTriggerBase):
    def __init__(self, hass: HomeAssistant, config: TriggerConfig) -> None: ...
    @override
    def _is_matching_item(self, item: TodoItem) -> bool: ...
    @override
    def _get_items_diff(self, old_item_ids: set[str], current_item_ids: set[str]) -> set[str]: ...

class ItemCompletedTrigger(ItemChangeTriggerBase):
    def __init__(self, hass: HomeAssistant, config: TriggerConfig) -> None: ...
    @override
    def _is_matching_item(self, item: TodoItem) -> bool: ...
    @override
    def _get_items_diff(self, old_item_ids: set[str], current_item_ids: set[str]) -> set[str]: ...

TRIGGERS: dict[str, type[Trigger]]

async def async_get_triggers(hass: HomeAssistant) -> dict[str, type[Trigger]]: ...

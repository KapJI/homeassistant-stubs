import dataclasses
from .const import ATTR_DESCRIPTION as ATTR_DESCRIPTION, ATTR_DUE as ATTR_DUE, ATTR_DUE_DATE as ATTR_DUE_DATE, ATTR_DUE_DATETIME as ATTR_DUE_DATETIME, ATTR_ITEM as ATTR_ITEM, ATTR_RENAME as ATTR_RENAME, ATTR_STATUS as ATTR_STATUS, DATA_COMPONENT as DATA_COMPONENT, DOMAIN as DOMAIN, TodoItemStatus as TodoItemStatus, TodoListEntityFeature as TodoListEntityFeature, TodoServices as TodoServices
from .entity import TodoItem as TodoItem, TodoListEntity as TodoListEntity, api_items_factory as api_items_factory
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, SupportsResponse as SupportsResponse, callback as callback
from homeassistant.exceptions import ServiceValidationError as ServiceValidationError
from typing import Any

@dataclasses.dataclass
class TodoItemFieldDescription:
    service_field: str
    todo_item_field: str
    validation: Callable[[Any], Any]
    required_feature: TodoListEntityFeature

TODO_ITEM_FIELDS: Incomplete
TODO_ITEM_FIELD_SCHEMA: Incomplete
TODO_ITEM_FIELD_VALIDATIONS: Incomplete
TODO_SERVICE_GET_ITEMS_SCHEMA: Incomplete

def _validate_supported_features(supported_features: int | None, call_data: dict[str, Any]) -> None: ...
def _find_by_uid_or_summary(value: str, items: list[TodoItem] | None) -> TodoItem | None: ...
async def _async_add_todo_item(entity: TodoListEntity, call: ServiceCall) -> None: ...
async def _async_update_todo_item(entity: TodoListEntity, call: ServiceCall) -> None: ...
async def _async_remove_todo_items(entity: TodoListEntity, call: ServiceCall) -> None: ...
async def _async_get_todo_items(entity: TodoListEntity, call: ServiceCall) -> dict[str, Any]: ...
async def _async_remove_completed_items(entity: TodoListEntity, _: ServiceCall) -> None: ...
@callback
def async_setup_services(hass: HomeAssistant) -> None: ...

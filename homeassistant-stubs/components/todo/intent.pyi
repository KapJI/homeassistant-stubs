from . import TodoItem as TodoItem, TodoItemStatus as TodoItemStatus, TodoListEntity as TodoListEntity
from .const import DATA_COMPONENT as DATA_COMPONENT, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import intent as intent

INTENT_LIST_ADD_ITEM: str
INTENT_LIST_COMPLETE_ITEM: str
INTENT_LIST_REMOVE_ITEM: str

async def async_setup_intents(hass: HomeAssistant) -> None: ...

class ListBaseIntentHandler(intent.IntentHandler):
    slot_schema: Incomplete
    platforms: Incomplete
    async def _async_do_handle(self, target_list: TodoListEntity, item: str) -> None: ...
    async def async_handle(self, intent_obj: intent.Intent) -> intent.IntentResponse: ...

class ListAddItemIntentHandler(ListBaseIntentHandler):
    intent_type = INTENT_LIST_ADD_ITEM
    description: str
    async def _async_do_handle(self, target_list: TodoListEntity, item: str) -> None: ...

class ListCompleteItemIntentHandler(ListBaseIntentHandler):
    intent_type = INTENT_LIST_COMPLETE_ITEM
    description: str
    async def _async_do_handle(self, target_list: TodoListEntity, item: str) -> None: ...

class ListRemoveItemIntentHandler(ListBaseIntentHandler):
    intent_type = INTENT_LIST_REMOVE_ITEM
    description: str
    async def _async_do_handle(self, target_list: TodoListEntity, item: str) -> None: ...

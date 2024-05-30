from . import DOMAIN as DOMAIN, TodoItem as TodoItem, TodoItemStatus as TodoItemStatus, TodoListEntity as TodoListEntity
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import intent as intent
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent

INTENT_LIST_ADD_ITEM: str

async def async_setup_intents(hass: HomeAssistant) -> None: ...

class ListAddItemIntent(intent.IntentHandler):
    intent_type = INTENT_LIST_ADD_ITEM
    description: str
    slot_schema: Incomplete
    platforms: Incomplete
    async def async_handle(self, intent_obj: intent.Intent) -> intent.IntentResponse: ...

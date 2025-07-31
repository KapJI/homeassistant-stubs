from . import OpenRouterConfigEntry as OpenRouterConfigEntry
from .entity import OpenRouterEntity as OpenRouterEntity
from _typeshed import Incomplete
from homeassistant.components import ai_task as ai_task, conversation as conversation
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.util.json import json_loads as json_loads

_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: OpenRouterConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class OpenRouterAITaskEntity(ai_task.AITaskEntity, OpenRouterEntity):
    _attr_name: Incomplete
    _attr_supported_features: Incomplete
    async def _async_generate_data(self, task: ai_task.GenDataTask, chat_log: conversation.ChatLog) -> ai_task.GenDataTaskResult: ...

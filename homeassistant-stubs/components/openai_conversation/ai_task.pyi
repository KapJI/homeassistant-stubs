from .entity import OpenAIBaseLLMEntity as OpenAIBaseLLMEntity
from _typeshed import Incomplete
from homeassistant.components import ai_task as ai_task, conversation as conversation
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.util.json import json_loads as json_loads

_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class OpenAITaskEntity(ai_task.AITaskEntity, OpenAIBaseLLMEntity):
    _attr_supported_features: Incomplete
    async def _async_generate_data(self, task: ai_task.GenDataTask, chat_log: conversation.ChatLog) -> ai_task.GenDataTaskResult: ...

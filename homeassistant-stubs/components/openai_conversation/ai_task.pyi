from . import OpenAIConfigEntry as OpenAIConfigEntry
from .const import CONF_CHAT_MODEL as CONF_CHAT_MODEL, CONF_IMAGE_MODEL as CONF_IMAGE_MODEL, RECOMMENDED_CHAT_MODEL as RECOMMENDED_CHAT_MODEL, RECOMMENDED_IMAGE_MODEL as RECOMMENDED_IMAGE_MODEL, UNSUPPORTED_IMAGE_MODELS as UNSUPPORTED_IMAGE_MODELS
from .entity import OpenAIBaseLLMEntity as OpenAIBaseLLMEntity
from _typeshed import Incomplete
from homeassistant.components import ai_task as ai_task, conversation as conversation
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigSubentry as ConfigSubentry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.util.json import json_loads as json_loads

_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class OpenAITaskEntity(ai_task.AITaskEntity, OpenAIBaseLLMEntity):
    _attr_supported_features: Incomplete
    def __init__(self, entry: OpenAIConfigEntry, subentry: ConfigSubentry) -> None: ...
    async def _async_generate_data(self, task: ai_task.GenDataTask, chat_log: conversation.ChatLog) -> ai_task.GenDataTaskResult: ...
    async def _async_generate_image(self, task: ai_task.GenImageTask, chat_log: conversation.ChatLog) -> ai_task.GenImageTaskResult: ...

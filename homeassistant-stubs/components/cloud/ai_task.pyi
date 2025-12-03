from .const import AI_TASK_ENTITY_UNIQUE_ID as AI_TASK_ENTITY_UNIQUE_ID, DATA_CLOUD as DATA_CLOUD
from .entity import BaseCloudLLMEntity as BaseCloudLLMEntity
from _typeshed import Incomplete
from hass_nabucasa.llm import LLMImageAttachment
from homeassistant.components import ai_task as ai_task, conversation as conversation
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.util.json import json_loads as json_loads

_LOGGER: Incomplete

def _convert_image_for_editing(data: bytes) -> tuple[bytes, str]: ...
async def async_prepare_image_generation_attachments(hass: HomeAssistant, attachments: list[conversation.Attachment]) -> list[LLMImageAttachment]: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class CloudAITaskEntity(BaseCloudLLMEntity, ai_task.AITaskEntity):
    _attr_has_entity_name: bool
    _attr_supported_features: Incomplete
    _attr_translation_key: str
    _attr_unique_id = AI_TASK_ENTITY_UNIQUE_ID
    @property
    def available(self) -> bool: ...
    async def _async_generate_data(self, task: ai_task.GenDataTask, chat_log: conversation.ChatLog) -> ai_task.GenDataTaskResult: ...
    async def _async_generate_image(self, task: ai_task.GenImageTask, chat_log: conversation.ChatLog) -> ai_task.GenImageTaskResult: ...

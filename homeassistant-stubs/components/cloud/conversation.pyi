from .const import CONVERSATION_ENTITY_UNIQUE_ID as CONVERSATION_ENTITY_UNIQUE_ID, DATA_CLOUD as DATA_CLOUD, DOMAIN as DOMAIN
from .entity import BaseCloudLLMEntity as BaseCloudLLMEntity
from _typeshed import Incomplete
from homeassistant.components import conversation as conversation
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import MATCH_ALL as MATCH_ALL
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import llm as llm
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Literal

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class CloudConversationEntity(BaseCloudLLMEntity, conversation.ConversationEntity):
    _attr_has_entity_name: bool
    _attr_name: str
    _attr_translation_key: str
    _attr_unique_id = CONVERSATION_ENTITY_UNIQUE_ID
    _attr_supported_features: Incomplete
    @property
    def available(self) -> bool: ...
    @property
    def supported_languages(self) -> list[str] | Literal['*']: ...
    async def _async_handle_message(self, user_input: conversation.ConversationInput, chat_log: conversation.ChatLog) -> conversation.ConversationResult: ...

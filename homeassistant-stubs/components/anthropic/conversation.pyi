from . import AnthropicConfigEntry as AnthropicConfigEntry
from .const import CONF_PROMPT as CONF_PROMPT, DOMAIN as DOMAIN
from .entity import AnthropicBaseLLMEntity as AnthropicBaseLLMEntity
from _typeshed import Incomplete
from homeassistant.components import conversation as conversation
from homeassistant.config_entries import ConfigSubentry as ConfigSubentry
from homeassistant.const import CONF_LLM_HASS_API as CONF_LLM_HASS_API, MATCH_ALL as MATCH_ALL
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Literal

async def async_setup_entry(hass: HomeAssistant, config_entry: AnthropicConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class AnthropicConversationEntity(conversation.ConversationEntity, conversation.AbstractConversationAgent, AnthropicBaseLLMEntity):
    _attr_supports_streaming: bool
    _attr_translation_key: str
    _attr_supported_features: Incomplete
    def __init__(self, entry: AnthropicConfigEntry, subentry: ConfigSubentry) -> None: ...
    @property
    def supported_languages(self) -> list[str] | Literal['*']: ...
    async def _async_handle_message(self, user_input: conversation.ConversationInput, chat_log: conversation.ChatLog) -> conversation.ConversationResult: ...

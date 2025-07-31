from . import OpenAIConfigEntry as OpenAIConfigEntry
from .const import CONF_PROMPT as CONF_PROMPT, DOMAIN as DOMAIN
from .entity import OpenAIBaseLLMEntity as OpenAIBaseLLMEntity
from _typeshed import Incomplete
from homeassistant.components import conversation as conversation
from homeassistant.config_entries import ConfigSubentry as ConfigSubentry
from homeassistant.const import CONF_LLM_HASS_API as CONF_LLM_HASS_API, MATCH_ALL as MATCH_ALL
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Literal

async def async_setup_entry(hass: HomeAssistant, config_entry: OpenAIConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class OpenAIConversationEntity(conversation.ConversationEntity, conversation.AbstractConversationAgent, OpenAIBaseLLMEntity):
    _attr_supports_streaming: bool
    _attr_supported_features: Incomplete
    def __init__(self, entry: OpenAIConfigEntry, subentry: ConfigSubentry) -> None: ...
    @property
    def supported_languages(self) -> list[str] | Literal['*']: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    async def _async_handle_message(self, user_input: conversation.ConversationInput, chat_log: conversation.ChatLog) -> conversation.ConversationResult: ...

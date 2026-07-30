from . import LlamaCppConfigEntry as LlamaCppConfigEntry
from .const import DOMAIN as DOMAIN
from .entity import LlamaCppBaseLLMEntity as LlamaCppBaseLLMEntity
from _typeshed import Incomplete
from homeassistant.components import conversation as conversation
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigSubentry as ConfigSubentry
from homeassistant.const import CONF_LLM_HASS_API as CONF_LLM_HASS_API, CONF_PROMPT as CONF_PROMPT, MATCH_ALL as MATCH_ALL
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Literal, override

async def async_setup_entry(hass: HomeAssistant, config_entry: LlamaCppConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class LlamaCppConversationEntity(conversation.ConversationEntity, conversation.AbstractConversationAgent, LlamaCppBaseLLMEntity):
    _attr_supported_features: Incomplete
    def __init__(self, entry: ConfigEntry, subentry: ConfigSubentry) -> None: ...
    @property
    @override
    def supported_languages(self) -> list[str] | Literal['*']: ...
    @override
    async def async_added_to_hass(self) -> None: ...
    @override
    async def async_will_remove_from_hass(self) -> None: ...
    @override
    async def _async_handle_message(self, user_input: conversation.ConversationInput, chat_log: conversation.ChatLog) -> conversation.ConversationResult: ...

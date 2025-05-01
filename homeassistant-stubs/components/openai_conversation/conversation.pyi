from . import OpenAIConfigEntry as OpenAIConfigEntry
from .const import CONF_CHAT_MODEL as CONF_CHAT_MODEL, CONF_MAX_TOKENS as CONF_MAX_TOKENS, CONF_PROMPT as CONF_PROMPT, CONF_REASONING_EFFORT as CONF_REASONING_EFFORT, CONF_TEMPERATURE as CONF_TEMPERATURE, CONF_TOP_P as CONF_TOP_P, CONF_WEB_SEARCH as CONF_WEB_SEARCH, CONF_WEB_SEARCH_CITY as CONF_WEB_SEARCH_CITY, CONF_WEB_SEARCH_CONTEXT_SIZE as CONF_WEB_SEARCH_CONTEXT_SIZE, CONF_WEB_SEARCH_COUNTRY as CONF_WEB_SEARCH_COUNTRY, CONF_WEB_SEARCH_REGION as CONF_WEB_SEARCH_REGION, CONF_WEB_SEARCH_TIMEZONE as CONF_WEB_SEARCH_TIMEZONE, CONF_WEB_SEARCH_USER_LOCATION as CONF_WEB_SEARCH_USER_LOCATION, DOMAIN as DOMAIN, LOGGER as LOGGER, RECOMMENDED_CHAT_MODEL as RECOMMENDED_CHAT_MODEL, RECOMMENDED_MAX_TOKENS as RECOMMENDED_MAX_TOKENS, RECOMMENDED_REASONING_EFFORT as RECOMMENDED_REASONING_EFFORT, RECOMMENDED_TEMPERATURE as RECOMMENDED_TEMPERATURE, RECOMMENDED_TOP_P as RECOMMENDED_TOP_P, RECOMMENDED_WEB_SEARCH_CONTEXT_SIZE as RECOMMENDED_WEB_SEARCH_CONTEXT_SIZE
from _typeshed import Incomplete
from collections.abc import AsyncGenerator, Callable as Callable
from homeassistant.components import assist_pipeline as assist_pipeline, conversation as conversation
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_LLM_HASS_API as CONF_LLM_HASS_API, MATCH_ALL as MATCH_ALL
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import intent as intent, llm as llm
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from openai._streaming import AsyncStream as AsyncStream
from openai.types.responses import FunctionToolParam, ResponseInputParam as ResponseInputParam, ResponseStreamEvent as ResponseStreamEvent, ToolParam as ToolParam
from typing import Any, Literal

MAX_TOOL_ITERATIONS: int

async def async_setup_entry(hass: HomeAssistant, config_entry: OpenAIConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...
def _format_tool(tool: llm.Tool, custom_serializer: Callable[[Any], Any] | None) -> FunctionToolParam: ...
def _convert_content_to_param(content: conversation.Content) -> ResponseInputParam: ...
async def _transform_stream(chat_log: conversation.ChatLog, result: AsyncStream[ResponseStreamEvent], messages: ResponseInputParam) -> AsyncGenerator[conversation.AssistantContentDeltaDict]: ...

class OpenAIConversationEntity(conversation.ConversationEntity, conversation.AbstractConversationAgent):
    _attr_has_entity_name: bool
    _attr_name: Incomplete
    entry: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    _attr_supported_features: Incomplete
    def __init__(self, entry: OpenAIConfigEntry) -> None: ...
    @property
    def supported_languages(self) -> list[str] | Literal['*']: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    async def _async_handle_message(self, user_input: conversation.ConversationInput, chat_log: conversation.ChatLog) -> conversation.ConversationResult: ...
    async def _async_entry_update_listener(self, hass: HomeAssistant, entry: ConfigEntry) -> None: ...

import voluptuous as vol
from . import LlamaCppConfigEntry as LlamaCppConfigEntry
from .api import api_error_handler as api_error_handler
from .const import CONF_CHAT_MODEL as CONF_CHAT_MODEL, CONF_MAX_TOKENS as CONF_MAX_TOKENS, CONF_STREAMING as CONF_STREAMING, CONF_TEMPERATURE as CONF_TEMPERATURE, CONF_TOP_P as CONF_TOP_P, DEFAULT_MODEL as DEFAULT_MODEL, DOMAIN as DOMAIN, LOGGER as LOGGER, RECOMMENDED_MAX_TOKENS as RECOMMENDED_MAX_TOKENS, RECOMMENDED_TEMPERATURE as RECOMMENDED_TEMPERATURE, RECOMMENDED_TOP_P as RECOMMENDED_TOP_P
from _typeshed import Incomplete
from collections.abc import AsyncGenerator, Callable as Callable
from homeassistant.components import conversation as conversation
from homeassistant.config_entries import ConfigSubentry as ConfigSubentry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import llm as llm
from homeassistant.helpers.entity import Entity as Entity
from openai import AsyncOpenAI as AsyncOpenAI
from openai._streaming import AsyncStream
from openai.types.chat import ChatCompletionChunk, ChatCompletionContentPartParam as ChatCompletionContentPartParam, ChatCompletionFunctionToolParam, ChatCompletionMessage as ChatCompletionMessage, ChatCompletionMessageParam
from openai.types.shared_params import ResponseFormatJSONSchema
from pathlib import Path
from typing import Any

MAX_TOOL_ITERATIONS: int
_LOGGER: Incomplete

def _format_structured_output(name: str, structure: vol.Schema, llm_api: llm.APIInstance | None) -> ResponseFormatJSONSchema: ...
def _format_tool(tool: llm.Tool, custom_serializer: Callable[[Any], Any] | None) -> ChatCompletionFunctionToolParam: ...
def _convert_content_to_chat_message(content: conversation.Content) -> ChatCompletionMessageParam | None: ...
def _decode_tool_arguments(arguments: str) -> Any: ...
async def _transform_response(message: ChatCompletionMessage) -> AsyncGenerator[conversation.AssistantContentDeltaDict]: ...
def _convert_content_to_param(content: conversation.Content) -> ChatCompletionMessageParam: ...
async def _transform_stream(result: AsyncStream[ChatCompletionChunk]) -> AsyncGenerator[conversation.AssistantContentDeltaDict]: ...

class LlamaCppBaseLLMEntity(Entity):
    _attr_has_entity_name: bool
    _attr_name: Incomplete
    entry: Incomplete
    subentry: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, entry: LlamaCppConfigEntry, subentry: ConfigSubentry) -> None: ...
    async def _async_handle_chat_log(self, chat_log: conversation.ChatLog, structure_name: str | None = None, structure: vol.Schema | None = None) -> None: ...

async def async_prepare_files_for_prompt(hass: HomeAssistant, files: list[Path]) -> list[ChatCompletionContentPartParam]: ...

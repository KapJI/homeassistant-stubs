import voluptuous as vol
from . import OpenAIConfigEntry as OpenAIConfigEntry
from .const import CONF_CHAT_MODEL as CONF_CHAT_MODEL, CONF_CODE_INTERPRETER as CONF_CODE_INTERPRETER, CONF_IMAGE_MODEL as CONF_IMAGE_MODEL, CONF_MAX_TOKENS as CONF_MAX_TOKENS, CONF_REASONING_EFFORT as CONF_REASONING_EFFORT, CONF_TEMPERATURE as CONF_TEMPERATURE, CONF_TOP_P as CONF_TOP_P, CONF_VERBOSITY as CONF_VERBOSITY, CONF_WEB_SEARCH as CONF_WEB_SEARCH, CONF_WEB_SEARCH_CITY as CONF_WEB_SEARCH_CITY, CONF_WEB_SEARCH_CONTEXT_SIZE as CONF_WEB_SEARCH_CONTEXT_SIZE, CONF_WEB_SEARCH_COUNTRY as CONF_WEB_SEARCH_COUNTRY, CONF_WEB_SEARCH_INLINE_CITATIONS as CONF_WEB_SEARCH_INLINE_CITATIONS, CONF_WEB_SEARCH_REGION as CONF_WEB_SEARCH_REGION, CONF_WEB_SEARCH_TIMEZONE as CONF_WEB_SEARCH_TIMEZONE, CONF_WEB_SEARCH_USER_LOCATION as CONF_WEB_SEARCH_USER_LOCATION, DOMAIN as DOMAIN, LOGGER as LOGGER, RECOMMENDED_CHAT_MODEL as RECOMMENDED_CHAT_MODEL, RECOMMENDED_IMAGE_MODEL as RECOMMENDED_IMAGE_MODEL, RECOMMENDED_MAX_TOKENS as RECOMMENDED_MAX_TOKENS, RECOMMENDED_REASONING_EFFORT as RECOMMENDED_REASONING_EFFORT, RECOMMENDED_TEMPERATURE as RECOMMENDED_TEMPERATURE, RECOMMENDED_TOP_P as RECOMMENDED_TOP_P, RECOMMENDED_VERBOSITY as RECOMMENDED_VERBOSITY, RECOMMENDED_WEB_SEARCH_CONTEXT_SIZE as RECOMMENDED_WEB_SEARCH_CONTEXT_SIZE, RECOMMENDED_WEB_SEARCH_INLINE_CITATIONS as RECOMMENDED_WEB_SEARCH_INLINE_CITATIONS, UNSUPPORTED_EXTENDED_CACHE_RETENTION_MODELS as UNSUPPORTED_EXTENDED_CACHE_RETENTION_MODELS
from _typeshed import Incomplete
from collections.abc import AsyncGenerator, Callable as Callable, Iterable
from homeassistant.components import conversation as conversation
from homeassistant.config_entries import ConfigSubentry as ConfigSubentry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import llm as llm
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.util import slugify as slugify
from openai._streaming import AsyncStream as AsyncStream
from openai.types.responses import FunctionToolParam, ResponseInputMessageContentListParam as ResponseInputMessageContentListParam, ResponseInputParam as ResponseInputParam, ResponseStreamEvent as ResponseStreamEvent, ToolParam as ToolParam
from pathlib import Path
from typing import Any

MAX_TOOL_ITERATIONS: int

def _adjust_schema(schema: dict[str, Any]) -> None: ...
def _format_structured_output(schema: vol.Schema, llm_api: llm.APIInstance | None) -> dict[str, Any]: ...
def _format_tool(tool: llm.Tool, custom_serializer: Callable[[Any], Any] | None) -> FunctionToolParam: ...
def _convert_content_to_param(chat_content: Iterable[conversation.Content]) -> ResponseInputParam: ...
async def _transform_stream(chat_log: conversation.ChatLog, stream: AsyncStream[ResponseStreamEvent], remove_citations: bool = False) -> AsyncGenerator[conversation.AssistantContentDeltaDict | conversation.ToolResultContentDeltaDict]: ...

class OpenAIBaseLLMEntity(Entity):
    _attr_has_entity_name: bool
    _attr_name: Incomplete
    entry: Incomplete
    subentry: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, entry: OpenAIConfigEntry, subentry: ConfigSubentry) -> None: ...
    async def _async_handle_chat_log(self, chat_log: conversation.ChatLog, structure_name: str | None = None, structure: vol.Schema | None = None, force_image: bool = False) -> None: ...

async def async_prepare_files_for_prompt(hass: HomeAssistant, files: list[tuple[Path, str | None]]) -> ResponseInputMessageContentListParam: ...

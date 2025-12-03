import voluptuous as vol
from .client import CloudClient as CloudClient
from _typeshed import Incomplete
from collections.abc import AsyncGenerator, Callable as Callable, Iterable
from enum import Enum
from hass_nabucasa import Cloud as Cloud
from homeassistant.components import conversation as conversation
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import llm as llm
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.util import slugify as slugify
from litellm import ResponseInputParam as ResponseInputParam
from openai.types.responses import FunctionToolParam as FunctionToolParam, ResponseInputItemParam as ResponseInputItemParam, ToolParam as ToolParam
from typing import Any, Literal

_LOGGER: Incomplete
_MAX_TOOL_ITERATIONS: int

class ResponseItemType(str, Enum):
    FUNCTION_CALL = 'function_call'
    MESSAGE = 'message'
    REASONING = 'reasoning'
    WEB_SEARCH_CALL = 'web_search_call'
    IMAGE = 'image'

def _convert_content_to_param(chat_content: Iterable[conversation.Content]) -> ResponseInputParam: ...
def _format_tool(tool: llm.Tool, custom_serializer: Callable[[Any], Any] | None) -> ToolParam: ...
def _adjust_schema(schema: dict[str, Any]) -> None: ...
def _format_structured_output(schema: vol.Schema, llm_api: llm.APIInstance | None) -> dict[str, Any]: ...
def _ensure_schema_constraints(schema: dict[str, Any]) -> None: ...
async def _transform_stream(chat_log: conversation.ChatLog, stream: Any, remove_citations: bool = False) -> AsyncGenerator[conversation.AssistantContentDeltaDict | conversation.ToolResultContentDeltaDict]: ...

class BaseCloudLLMEntity(Entity):
    _cloud: Incomplete
    _entry: Incomplete
    def __init__(self, cloud: Cloud[CloudClient], config_entry: ConfigEntry) -> None: ...
    async def _prepare_chat_for_generation(self, chat_log: conversation.ChatLog, messages: ResponseInputParam, response_format: dict[str, Any] | None = None) -> dict[str, Any]: ...
    async def _async_prepare_files_for_prompt(self, attachments: list[conversation.Attachment]) -> list[dict[str, Any]]: ...
    async def _async_handle_chat_log(self, type: Literal['ai_task', 'conversation'], chat_log: conversation.ChatLog, structure_name: str | None = None, structure: vol.Schema | None = None) -> None: ...

import voluptuous as vol
from . import OpenRouterConfigEntry as OpenRouterConfigEntry
from .const import DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from collections.abc import AsyncGenerator, Callable as Callable
from homeassistant.components import conversation as conversation
from homeassistant.config_entries import ConfigSubentry as ConfigSubentry
from homeassistant.const import CONF_MODEL as CONF_MODEL
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import llm as llm
from homeassistant.helpers.entity import Entity as Entity
from openai.types.chat import ChatCompletionContentPartImageParam as ChatCompletionContentPartImageParam, ChatCompletionFunctionToolParam, ChatCompletionMessage as ChatCompletionMessage, ChatCompletionMessageParam as ChatCompletionMessageParam
from openai.types.shared_params.response_format_json_schema import JSONSchema as JSONSchema
from pathlib import Path
from typing import Any

MAX_TOOL_ITERATIONS: int

def _adjust_schema(schema: dict[str, Any]) -> None: ...
def _format_structured_output(name: str, schema: vol.Schema, llm_api: llm.APIInstance | None) -> JSONSchema: ...
def _format_tool(tool: llm.Tool, custom_serializer: Callable[[Any], Any] | None) -> ChatCompletionFunctionToolParam: ...
def _convert_content_to_chat_message(content: conversation.Content) -> ChatCompletionMessageParam | None: ...
def _decode_tool_arguments(arguments: str) -> Any: ...
async def _transform_response(message: ChatCompletionMessage) -> AsyncGenerator[conversation.AssistantContentDeltaDict]: ...
async def async_prepare_files_for_prompt(hass: HomeAssistant, files: list[tuple[Path, str | None]]) -> list[ChatCompletionContentPartImageParam]: ...

class OpenRouterEntity(Entity):
    _attr_has_entity_name: bool
    entry: Incomplete
    subentry: Incomplete
    model: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, entry: OpenRouterConfigEntry, subentry: ConfigSubentry) -> None: ...
    async def _async_handle_chat_log(self, chat_log: conversation.ChatLog, structure_name: str | None = None, structure: vol.Schema | None = None) -> None: ...

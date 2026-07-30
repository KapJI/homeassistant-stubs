from .const import DOMAIN as DOMAIN, LOGGER as LOGGER
from .coordinator import LiteLLMConfigEntry as LiteLLMConfigEntry, LiteLLMDataUpdateCoordinator as LiteLLMDataUpdateCoordinator
from _typeshed import Incomplete
from collections.abc import AsyncGenerator, Callable as Callable
from homeassistant.components import conversation as conversation
from homeassistant.config_entries import ConfigSubentry as ConfigSubentry
from homeassistant.const import CONF_MODEL as CONF_MODEL
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import llm as llm
from homeassistant.helpers.json import json_dumps as json_dumps
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from openai.types.chat import ChatCompletionFunctionToolParam, ChatCompletionMessage as ChatCompletionMessage, ChatCompletionMessageParam as ChatCompletionMessageParam
from typing import Any

MAX_TOOL_ITERATIONS: int

def _format_tool(tool: llm.Tool, custom_serializer: Callable[[Any], Any] | None) -> ChatCompletionFunctionToolParam: ...
def _convert_content_to_chat_message(content: conversation.Content) -> ChatCompletionMessageParam | None: ...
def _decode_tool_arguments(arguments: str) -> Any: ...
async def _transform_response(message: ChatCompletionMessage) -> AsyncGenerator[conversation.AssistantContentDeltaDict]: ...

class LiteLLMEntity(CoordinatorEntity[LiteLLMDataUpdateCoordinator]):
    _attr_has_entity_name: bool
    entry: Incomplete
    subentry: Incomplete
    model: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, entry: LiteLLMConfigEntry, subentry: ConfigSubentry) -> None: ...
    async def _async_handle_chat_log(self, chat_log: conversation.ChatLog) -> None: ...

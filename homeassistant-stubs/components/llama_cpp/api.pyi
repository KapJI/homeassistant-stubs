import openai
from .const import CONF_BASE_URL as CONF_BASE_URL, DEFAULT_API_KEY as DEFAULT_API_KEY, DEFAULT_MODEL as DEFAULT_MODEL, DOMAIN as DOMAIN, RECOMMENDED_CHAT_MODELS as RECOMMENDED_CHAT_MODELS
from _typeshed import Incomplete
from collections.abc import Generator, Mapping
from contextlib import contextmanager
from homeassistant.const import CONF_API_KEY as CONF_API_KEY
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.httpx_client import get_async_client as get_async_client
from openai.types.chat import ChatCompletionMessageParam as ChatCompletionMessageParam, ChatCompletionToolParam as ChatCompletionToolParam
from typing import Any

_LOGGER: Incomplete
_TEST_MESSAGES: list[ChatCompletionMessageParam]
_TEST_TOOLS: list[ChatCompletionToolParam]
_TEST_MAX_TOKENS: int

async def async_create_client(hass: HomeAssistant, config_entry_data: Mapping[str, Any]) -> openai.AsyncOpenAI: ...
async def async_list_models(client: openai.AsyncOpenAI) -> list[str]: ...
async def async_validate_completions(client: openai.AsyncOpenAI, model: str, stream: bool = False) -> None: ...
def recommended_model(models: list[str] | None) -> str: ...
def model_name_to_title(model_id: str) -> str: ...
def _extract_error_message(err: openai.APIStatusError) -> str: ...
@contextmanager
def api_error_handler() -> Generator[None]: ...

import openai
from .api import async_create_client as async_create_client, async_list_models as async_list_models, async_validate_completions as async_validate_completions, model_name_to_title as model_name_to_title, recommended_model as recommended_model
from .const import CONF_BASE_URL as CONF_BASE_URL, CONF_CHAT_MODEL as CONF_CHAT_MODEL, CONF_MAX_TOKENS as CONF_MAX_TOKENS, CONF_RECOMMENDED as CONF_RECOMMENDED, CONF_STREAMING as CONF_STREAMING, CONF_TEMPERATURE as CONF_TEMPERATURE, CONF_TOP_P as CONF_TOP_P, DEFAULT_BASE_URL as DEFAULT_BASE_URL, DOMAIN as DOMAIN, LOGGER as LOGGER, RECOMMENDED_MAX_TOKENS as RECOMMENDED_MAX_TOKENS, RECOMMENDED_TEMPERATURE as RECOMMENDED_TEMPERATURE, RECOMMENDED_TOP_P as RECOMMENDED_TOP_P
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigEntryState as ConfigEntryState, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, ConfigSubentryFlow as ConfigSubentryFlow, SubentryFlowResult as SubentryFlowResult
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_LLM_HASS_API as CONF_LLM_HASS_API, CONF_PROMPT as CONF_PROMPT
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import llm as llm
from homeassistant.helpers.selector import NumberSelector as NumberSelector, NumberSelectorConfig as NumberSelectorConfig, SelectOptionDict as SelectOptionDict, SelectSelector as SelectSelector, SelectSelectorConfig as SelectSelectorConfig, SelectSelectorMode as SelectSelectorMode, TemplateSelector as TemplateSelector
from typing import Any, override

_LOGGER: Incomplete
STEP_USER_DATA_SCHEMA: Incomplete

class LlamaCppConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    data: dict[str, Any] | None
    client: openai.AsyncOpenAI | None
    models: list[str] | None
    @override
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_model(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    @classmethod
    @callback
    @override
    def async_get_supported_subentry_types(cls, config_entry: ConfigEntry) -> dict[str, type[ConfigSubentryFlow]]: ...

class ConversationSubentryFlowHandler(ConfigSubentryFlow):
    last_rendered_recommended: bool
    options: dict[str, Any] | None
    models: list[str] | None
    @property
    def _openai_client(self) -> openai.AsyncOpenAI: ...
    async def _get_models(self) -> list[str] | None: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> SubentryFlowResult: ...
    async def async_step_reconfigure(self, user_input: dict[str, Any] | None = None) -> SubentryFlowResult: ...
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> SubentryFlowResult: ...

def llama_cpp_config_option_schema(hass: HomeAssistant, options: dict[str, Any], models: list[str] | None = None) -> dict: ...

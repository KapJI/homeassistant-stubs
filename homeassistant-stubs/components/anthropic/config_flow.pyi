import anthropic
from . import AnthropicConfigEntry as AnthropicConfigEntry
from .const import CONF_CHAT_MODEL as CONF_CHAT_MODEL, CONF_CODE_EXECUTION as CONF_CODE_EXECUTION, CONF_MAX_TOKENS as CONF_MAX_TOKENS, CONF_PROMPT as CONF_PROMPT, CONF_PROMPT_CACHING as CONF_PROMPT_CACHING, CONF_RECOMMENDED as CONF_RECOMMENDED, CONF_THINKING_BUDGET as CONF_THINKING_BUDGET, CONF_THINKING_EFFORT as CONF_THINKING_EFFORT, CONF_TOOL_SEARCH as CONF_TOOL_SEARCH, CONF_WEB_SEARCH as CONF_WEB_SEARCH, CONF_WEB_SEARCH_CITY as CONF_WEB_SEARCH_CITY, CONF_WEB_SEARCH_COUNTRY as CONF_WEB_SEARCH_COUNTRY, CONF_WEB_SEARCH_MAX_USES as CONF_WEB_SEARCH_MAX_USES, CONF_WEB_SEARCH_REGION as CONF_WEB_SEARCH_REGION, CONF_WEB_SEARCH_TIMEZONE as CONF_WEB_SEARCH_TIMEZONE, CONF_WEB_SEARCH_USER_LOCATION as CONF_WEB_SEARCH_USER_LOCATION, DEFAULT as DEFAULT, DEFAULT_AI_TASK_NAME as DEFAULT_AI_TASK_NAME, DEFAULT_CONVERSATION_NAME as DEFAULT_CONVERSATION_NAME, DOMAIN as DOMAIN, MIN_THINKING_BUDGET as MIN_THINKING_BUDGET, PromptCaching as PromptCaching, TOOL_SEARCH_UNSUPPORTED_MODELS as TOOL_SEARCH_UNSUPPORTED_MODELS
from .coordinator import model_alias as model_alias
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.components.zone import ENTITY_ID_HOME as ENTITY_ID_HOME
from homeassistant.config_entries import ConfigEntryState as ConfigEntryState, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, ConfigSubentryFlow as ConfigSubentryFlow, SOURCE_REAUTH as SOURCE_REAUTH, SubentryFlowResult as SubentryFlowResult
from homeassistant.const import ATTR_LATITUDE as ATTR_LATITUDE, ATTR_LONGITUDE as ATTR_LONGITUDE, CONF_API_KEY as CONF_API_KEY, CONF_LLM_HASS_API as CONF_LLM_HASS_API, CONF_NAME as CONF_NAME
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import llm as llm
from homeassistant.helpers.httpx_client import get_async_client as get_async_client
from homeassistant.helpers.selector import NumberSelector as NumberSelector, NumberSelectorConfig as NumberSelectorConfig, SelectOptionDict as SelectOptionDict, SelectSelector as SelectSelector, SelectSelectorConfig as SelectSelectorConfig, SelectSelectorMode as SelectSelectorMode, TemplateSelector as TemplateSelector
from homeassistant.helpers.typing import VolDictType as VolDictType
from typing import Any

_LOGGER: Incomplete
STEP_USER_DATA_SCHEMA: Incomplete
DEFAULT_CONVERSATION_OPTIONS: Incomplete
DEFAULT_AI_TASK_OPTIONS: Incomplete

async def validate_input(hass: HomeAssistant, data: dict[str, Any]) -> None: ...

class AnthropicConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    MINOR_VERSION: int
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    @classmethod
    @callback
    def async_get_supported_subentry_types(cls, config_entry: AnthropicConfigEntry) -> dict[str, type[ConfigSubentryFlow]]: ...

class ConversationSubentryFlowHandler(ConfigSubentryFlow):
    options: dict[str, Any]
    model_info: anthropic.types.ModelInfo
    @property
    def _is_new(self) -> bool: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> SubentryFlowResult: ...
    async def async_step_reconfigure(self, user_input: dict[str, Any] | None = None) -> SubentryFlowResult: ...
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> SubentryFlowResult: ...
    async def async_step_advanced(self, user_input: dict[str, Any] | None = None) -> SubentryFlowResult: ...
    async def async_step_model(self, user_input: dict[str, Any] | None = None) -> SubentryFlowResult: ...
    def _get_model_list(self) -> list[SelectOptionDict]: ...
    async def _get_location_data(self) -> dict[str, str]: ...

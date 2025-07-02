from .const import CONF_CHAT_MODEL as CONF_CHAT_MODEL, CONF_MAX_TOKENS as CONF_MAX_TOKENS, CONF_PROMPT as CONF_PROMPT, CONF_REASONING_EFFORT as CONF_REASONING_EFFORT, CONF_RECOMMENDED as CONF_RECOMMENDED, CONF_TEMPERATURE as CONF_TEMPERATURE, CONF_TOP_P as CONF_TOP_P, CONF_WEB_SEARCH as CONF_WEB_SEARCH, CONF_WEB_SEARCH_CITY as CONF_WEB_SEARCH_CITY, CONF_WEB_SEARCH_CONTEXT_SIZE as CONF_WEB_SEARCH_CONTEXT_SIZE, CONF_WEB_SEARCH_COUNTRY as CONF_WEB_SEARCH_COUNTRY, CONF_WEB_SEARCH_REGION as CONF_WEB_SEARCH_REGION, CONF_WEB_SEARCH_TIMEZONE as CONF_WEB_SEARCH_TIMEZONE, CONF_WEB_SEARCH_USER_LOCATION as CONF_WEB_SEARCH_USER_LOCATION, DEFAULT_CONVERSATION_NAME as DEFAULT_CONVERSATION_NAME, DOMAIN as DOMAIN, RECOMMENDED_CHAT_MODEL as RECOMMENDED_CHAT_MODEL, RECOMMENDED_MAX_TOKENS as RECOMMENDED_MAX_TOKENS, RECOMMENDED_REASONING_EFFORT as RECOMMENDED_REASONING_EFFORT, RECOMMENDED_TEMPERATURE as RECOMMENDED_TEMPERATURE, RECOMMENDED_TOP_P as RECOMMENDED_TOP_P, RECOMMENDED_WEB_SEARCH as RECOMMENDED_WEB_SEARCH, RECOMMENDED_WEB_SEARCH_CONTEXT_SIZE as RECOMMENDED_WEB_SEARCH_CONTEXT_SIZE, RECOMMENDED_WEB_SEARCH_USER_LOCATION as RECOMMENDED_WEB_SEARCH_USER_LOCATION, UNSUPPORTED_MODELS as UNSUPPORTED_MODELS, WEB_SEARCH_MODELS as WEB_SEARCH_MODELS
from _typeshed import Incomplete
from homeassistant.components.zone import ENTITY_ID_HOME as ENTITY_ID_HOME
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigEntryState as ConfigEntryState, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, ConfigSubentryFlow as ConfigSubentryFlow, SubentryFlowResult as SubentryFlowResult
from homeassistant.const import ATTR_LATITUDE as ATTR_LATITUDE, ATTR_LONGITUDE as ATTR_LONGITUDE, CONF_API_KEY as CONF_API_KEY, CONF_LLM_HASS_API as CONF_LLM_HASS_API, CONF_NAME as CONF_NAME
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import llm as llm
from homeassistant.helpers.httpx_client import get_async_client as get_async_client
from homeassistant.helpers.selector import NumberSelector as NumberSelector, NumberSelectorConfig as NumberSelectorConfig, SelectOptionDict as SelectOptionDict, SelectSelector as SelectSelector, SelectSelectorConfig as SelectSelectorConfig, SelectSelectorMode as SelectSelectorMode, TemplateSelector as TemplateSelector
from homeassistant.helpers.typing import VolDictType as VolDictType
from typing import Any

_LOGGER: Incomplete
STEP_USER_DATA_SCHEMA: Incomplete
RECOMMENDED_OPTIONS: Incomplete

async def validate_input(hass: HomeAssistant, data: dict[str, Any]) -> None: ...

class OpenAIConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    MINOR_VERSION: int
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    @classmethod
    @callback
    def async_get_supported_subentry_types(cls, config_entry: ConfigEntry) -> dict[str, type[ConfigSubentryFlow]]: ...

class ConversationSubentryFlowHandler(ConfigSubentryFlow):
    last_rendered_recommended: bool
    options: dict[str, Any]
    @property
    def _is_new(self) -> bool: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> SubentryFlowResult: ...
    async def async_step_reconfigure(self, user_input: dict[str, Any] | None = None) -> SubentryFlowResult: ...
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> SubentryFlowResult: ...
    async def async_step_advanced(self, user_input: dict[str, Any] | None = None) -> SubentryFlowResult: ...
    async def async_step_model(self, user_input: dict[str, Any] | None = None) -> SubentryFlowResult: ...
    async def _get_location_data(self) -> dict[str, str]: ...

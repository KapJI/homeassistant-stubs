from .const import CONF_PROMPT as CONF_PROMPT, DOMAIN as DOMAIN, RECOMMENDED_CONVERSATION_OPTIONS as RECOMMENDED_CONVERSATION_OPTIONS
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, ConfigSubentryFlow as ConfigSubentryFlow, SubentryFlowResult as SubentryFlowResult
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_LLM_HASS_API as CONF_LLM_HASS_API, CONF_MODEL as CONF_MODEL
from homeassistant.core import callback as callback
from homeassistant.helpers import llm as llm
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.selector import SelectOptionDict as SelectOptionDict, SelectSelector as SelectSelector, SelectSelectorConfig as SelectSelectorConfig, SelectSelectorMode as SelectSelectorMode, TemplateSelector as TemplateSelector
from python_open_router import Model as Model
from typing import Any

_LOGGER: Incomplete

class OpenRouterConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    @classmethod
    @callback
    def async_get_supported_subentry_types(cls, config_entry: ConfigEntry) -> dict[str, type[ConfigSubentryFlow]]: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...

class OpenRouterSubentryFlowHandler(ConfigSubentryFlow):
    models: dict[str, Model]
    def __init__(self) -> None: ...
    async def _get_models(self) -> None: ...

class ConversationFlowHandler(OpenRouterSubentryFlowHandler):
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> SubentryFlowResult: ...

class AITaskDataFlowHandler(OpenRouterSubentryFlowHandler):
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> SubentryFlowResult: ...

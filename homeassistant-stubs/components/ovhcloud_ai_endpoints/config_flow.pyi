from . import _create_client as _create_client, _validate_api_key as _validate_api_key
from .const import CONF_PROMPT as CONF_PROMPT, DOMAIN as DOMAIN, RECOMMENDED_CONVERSATION_OPTIONS as RECOMMENDED_CONVERSATION_OPTIONS
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigEntryState as ConfigEntryState, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, ConfigSubentryFlow as ConfigSubentryFlow, SubentryFlowResult as SubentryFlowResult
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_LLM_HASS_API as CONF_LLM_HASS_API, CONF_MODEL as CONF_MODEL
from homeassistant.core import callback as callback
from homeassistant.helpers import llm as llm
from homeassistant.helpers.selector import SelectOptionDict as SelectOptionDict, SelectSelector as SelectSelector, SelectSelectorConfig as SelectSelectorConfig, SelectSelectorMode as SelectSelectorMode, TemplateSelector as TemplateSelector
from openai import AsyncOpenAI as AsyncOpenAI
from typing import Any, override

_LOGGER: Incomplete
STEP_REAUTH_DATA_SCHEMA: Incomplete

class OVHcloudAIEndpointsConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    MINOR_VERSION: int
    @classmethod
    @callback
    @override
    def async_get_supported_subentry_types(cls, config_entry: ConfigEntry) -> dict[str, type[ConfigSubentryFlow]]: ...
    @override
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reconfigure(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...

class ConversationFlowHandler(ConfigSubentryFlow):
    models: list[str]
    options: dict[str, Any]
    def __init__(self) -> None: ...
    async def _get_models(self) -> None: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> SubentryFlowResult: ...
    async def async_step_reconfigure(self, user_input: dict[str, Any] | None = None) -> SubentryFlowResult: ...
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> SubentryFlowResult: ...

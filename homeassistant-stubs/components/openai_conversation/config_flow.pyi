from .const import CONF_CHAT_MODEL as CONF_CHAT_MODEL, CONF_MAX_TOKENS as CONF_MAX_TOKENS, CONF_PROMPT as CONF_PROMPT, CONF_REASONING_EFFORT as CONF_REASONING_EFFORT, CONF_RECOMMENDED as CONF_RECOMMENDED, CONF_TEMPERATURE as CONF_TEMPERATURE, CONF_TOP_P as CONF_TOP_P, CONF_WEB_SEARCH as CONF_WEB_SEARCH, CONF_WEB_SEARCH_CITY as CONF_WEB_SEARCH_CITY, CONF_WEB_SEARCH_CONTEXT_SIZE as CONF_WEB_SEARCH_CONTEXT_SIZE, CONF_WEB_SEARCH_COUNTRY as CONF_WEB_SEARCH_COUNTRY, CONF_WEB_SEARCH_REGION as CONF_WEB_SEARCH_REGION, CONF_WEB_SEARCH_TIMEZONE as CONF_WEB_SEARCH_TIMEZONE, CONF_WEB_SEARCH_USER_LOCATION as CONF_WEB_SEARCH_USER_LOCATION, DOMAIN as DOMAIN, RECOMMENDED_CHAT_MODEL as RECOMMENDED_CHAT_MODEL, RECOMMENDED_MAX_TOKENS as RECOMMENDED_MAX_TOKENS, RECOMMENDED_REASONING_EFFORT as RECOMMENDED_REASONING_EFFORT, RECOMMENDED_TEMPERATURE as RECOMMENDED_TEMPERATURE, RECOMMENDED_TOP_P as RECOMMENDED_TOP_P, RECOMMENDED_WEB_SEARCH as RECOMMENDED_WEB_SEARCH, RECOMMENDED_WEB_SEARCH_CONTEXT_SIZE as RECOMMENDED_WEB_SEARCH_CONTEXT_SIZE, RECOMMENDED_WEB_SEARCH_USER_LOCATION as RECOMMENDED_WEB_SEARCH_USER_LOCATION, UNSUPPORTED_MODELS as UNSUPPORTED_MODELS, WEB_SEARCH_MODELS as WEB_SEARCH_MODELS
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.components.zone import ENTITY_ID_HOME as ENTITY_ID_HOME
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, OptionsFlow as OptionsFlow
from homeassistant.const import ATTR_LATITUDE as ATTR_LATITUDE, ATTR_LONGITUDE as ATTR_LONGITUDE, CONF_API_KEY as CONF_API_KEY, CONF_LLM_HASS_API as CONF_LLM_HASS_API
from homeassistant.core import HomeAssistant as HomeAssistant
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
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    @staticmethod
    def async_get_options_flow(config_entry: ConfigEntry) -> OptionsFlow: ...

class OpenAIOptionsFlow(OptionsFlow):
    last_rendered_recommended: Incomplete
    def __init__(self, config_entry: ConfigEntry) -> None: ...
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def get_location_data(self) -> dict[str, str]: ...

def openai_config_option_schema(hass: HomeAssistant, options: Mapping[str, Any]) -> VolDictType: ...

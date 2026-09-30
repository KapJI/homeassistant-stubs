import probatio
from .const import CONF_ALL_LLM_APIS as CONF_ALL_LLM_APIS, CONF_REQUIRE_ADMIN as CONF_REQUIRE_ADMIN, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, OptionsFlow as OptionsFlow
from homeassistant.const import CONF_LLM_HASS_API as CONF_LLM_HASS_API
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import llm as llm
from homeassistant.helpers.selector import BooleanSelector as BooleanSelector, SelectOptionDict as SelectOptionDict, SelectSelector as SelectSelector, SelectSelectorConfig as SelectSelectorConfig
from typing import Any, override

_LOGGER: Incomplete
MORE_INFO_URL: str
ALL_LLM_APIS_TITLE: str

def _llm_api_names(hass: HomeAssistant) -> dict[str, str]: ...
def _llm_api_title(llm_apis: dict[str, str], all_llm_apis: bool, api_ids: list[str]) -> str: ...
def _selected_llm_apis(entry: ConfigEntry, llm_apis: dict[str, str]) -> list[str]: ...
def _options_schema(llm_apis: dict[str, str], all_llm_apis: bool, default: list[str], require_admin: bool) -> probatio.Schema: ...

class ModelContextServerProtocolConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    MINOR_VERSION: int
    @staticmethod
    @callback
    @override
    def async_get_options_flow(config_entry: ConfigEntry) -> ModelContextServerProtocolOptionsFlow: ...
    @override
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...

class ModelContextServerProtocolOptionsFlow(OptionsFlow):
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...

from .const import CONF_PROFILE_ID as CONF_PROFILE_ID, DOMAIN as DOMAIN, SUBENTRY_TYPE_PROFILE as SUBENTRY_TYPE_PROFILE
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigEntryState as ConfigEntryState, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, ConfigSubentryFlow as ConfigSubentryFlow, SubentryFlowResult as SubentryFlowResult
from homeassistant.const import CONF_API_KEY as CONF_API_KEY
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.selector import SelectOptionDict as SelectOptionDict, SelectSelector as SelectSelector, SelectSelectorConfig as SelectSelectorConfig, SelectSelectorMode as SelectSelectorMode
from nextdns import NextDns
from typing import Any, override

AUTH_SCHEMA: Incomplete
_LOGGER: Incomplete

async def async_init_nextdns(hass: HomeAssistant, api_key: str) -> NextDns: ...
async def async_validate_new_api_key(hass: HomeAssistant, user_input: dict[str, Any], profile_ids: list[str]) -> dict[str, str]: ...

class NextDnsFlowHandler(ConfigFlow, domain=DOMAIN):
    VERSION: int
    nextdns: NextDns
    api_key: str
    def __init__(self) -> None: ...
    @override
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_profiles(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reconfigure(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    @classmethod
    @callback
    @override
    def async_get_supported_subentry_types(cls, config_entry: ConfigEntry) -> dict[str, type[ConfigSubentryFlow]]: ...

class ProfileSubentryFlowHandler(ConfigSubentryFlow):
    nextdns: NextDns
    def __init__(self) -> None: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> SubentryFlowResult: ...

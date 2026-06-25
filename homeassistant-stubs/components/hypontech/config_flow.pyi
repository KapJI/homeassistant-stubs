import voluptuous as vol
from .const import CONF_OEM as CONF_OEM, DEFAULT_OEM as DEFAULT_OEM, DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, SOURCE_USER as SOURCE_USER
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.selector import SelectOptionDict as SelectOptionDict, SelectSelector as SelectSelector, SelectSelectorConfig as SelectSelectorConfig, SelectSelectorMode as SelectSelectorMode
from hyponcloud import AdminInfo as AdminInfo
from typing import Any, override

_LOGGER: Incomplete
OEM_OPTIONS: Incomplete
STEP_REAUTH_DATA_SCHEMA: Incomplete

def _data_schema(default_oem: int = ...) -> vol.Schema: ...
def _entry_data(user_input: Mapping[str, Any]) -> dict[str, Any]: ...
def _unique_id(account_id: str, oem: int) -> str: ...

class HypontechConfigFlow(ConfigFlow, domain=DOMAIN):
    _default_oem: Incomplete
    def __init__(self) -> None: ...
    async def _async_validate_input(self, entry_data: Mapping[str, Any]) -> tuple[AdminInfo | None, dict[str, str]]: ...
    @override
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...

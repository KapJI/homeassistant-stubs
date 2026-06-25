from . import SmtpConfigEntry as SmtpConfigEntry
from .const import CONF_ENCRYPTION as CONF_ENCRYPTION, CONF_SENDER_NAME as CONF_SENDER_NAME, CONF_SERVER as CONF_SERVER, DEFAULT_ENCRYPTION as DEFAULT_ENCRYPTION, DEFAULT_HOST as DEFAULT_HOST, DEFAULT_PORT as DEFAULT_PORT, DEFAULT_TIMEOUT as DEFAULT_TIMEOUT, DOMAIN as DOMAIN, ENCRYPTION_OPTIONS as ENCRYPTION_OPTIONS, SUBENTRY_TYPE_RECIPIENT as SUBENTRY_TYPE_RECIPIENT
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, ConfigSubentryData as ConfigSubentryData, ConfigSubentryFlow as ConfigSubentryFlow, FlowType as FlowType, OptionsFlow as OptionsFlow, SOURCE_USER as SOURCE_USER, SubentryFlowContext as SubentryFlowContext, SubentryFlowResult as SubentryFlowResult
from homeassistant.const import CONF_NAME as CONF_NAME, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, CONF_RECIPIENT as CONF_RECIPIENT, CONF_SENDER as CONF_SENDER, CONF_TIMEOUT as CONF_TIMEOUT, CONF_USERNAME as CONF_USERNAME, CONF_VERIFY_SSL as CONF_VERIFY_SSL, UnitOfTime as UnitOfTime
from homeassistant.core import callback as callback
from homeassistant.helpers.selector import NumberSelector as NumberSelector, NumberSelectorConfig as NumberSelectorConfig, NumberSelectorMode as NumberSelectorMode, SelectSelector as SelectSelector, SelectSelectorConfig as SelectSelectorConfig, SelectSelectorMode as SelectSelectorMode, TextSelector as TextSelector, TextSelectorConfig as TextSelectorConfig, TextSelectorType as TextSelectorType
from homeassistant.util.ssl import create_client_context as create_client_context
from typing import Any, override

_LOGGER: Incomplete
STEP_USER_DATA_SCHEMA: Incomplete
STEP_REAUTH_DATA_SCHEMA: Incomplete
OPTIONS_SCHEMA: Incomplete

class MailConfigFlow(ConfigFlow, domain=DOMAIN):
    @classmethod
    @callback
    @override
    def async_get_supported_subentry_types(cls, config_entry: SmtpConfigEntry) -> dict[str, type[ConfigSubentryFlow]]: ...
    @staticmethod
    @callback
    @override
    def async_get_options_flow(config_entry: SmtpConfigEntry) -> OptionsFlowHandler: ...
    @override
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    @override
    async def async_on_create_entry(self, result: ConfigFlowResult) -> ConfigFlowResult: ...
    async def async_step_reconfigure(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_import(self, import_info: dict[str, Any]) -> ConfigFlowResult: ...

def validate_input(user_input: dict[str, Any]) -> dict[str, str]: ...

class RecipientSubentryFlowHandler(ConfigSubentryFlow):
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> SubentryFlowResult: ...

class OptionsFlowHandler(OptionsFlow):
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...

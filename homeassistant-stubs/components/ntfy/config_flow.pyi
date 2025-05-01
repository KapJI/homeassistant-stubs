from .const import CONF_TOPIC as CONF_TOPIC, DEFAULT_URL as DEFAULT_URL, DOMAIN as DOMAIN, SECTION_AUTH as SECTION_AUTH
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant import data_entry_flow as data_entry_flow
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, ConfigSubentryFlow as ConfigSubentryFlow, SubentryFlowResult as SubentryFlowResult
from homeassistant.const import ATTR_CREDENTIALS as ATTR_CREDENTIALS, CONF_NAME as CONF_NAME, CONF_PASSWORD as CONF_PASSWORD, CONF_TOKEN as CONF_TOKEN, CONF_URL as CONF_URL, CONF_USERNAME as CONF_USERNAME, CONF_VERIFY_SSL as CONF_VERIFY_SSL
from homeassistant.core import callback as callback
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.selector import TextSelector as TextSelector, TextSelectorConfig as TextSelectorConfig, TextSelectorType as TextSelectorType
from typing import Any

_LOGGER: Incomplete
STEP_USER_DATA_SCHEMA: Incomplete
STEP_REAUTH_DATA_SCHEMA: Incomplete
STEP_USER_TOPIC_SCHEMA: Incomplete
RE_TOPIC: Incomplete

class NtfyConfigFlow(ConfigFlow, domain=DOMAIN):
    @classmethod
    @callback
    def async_get_supported_subentry_types(cls, config_entry: ConfigEntry) -> dict[str, type[ConfigSubentryFlow]]: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...

class TopicSubentryFlowHandler(ConfigSubentryFlow):
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> SubentryFlowResult: ...
    async def async_step_generate_topic(self, user_input: dict[str, Any] | None = None) -> SubentryFlowResult: ...
    async def async_step_add_topic(self, user_input: dict[str, Any] | None = None) -> SubentryFlowResult: ...

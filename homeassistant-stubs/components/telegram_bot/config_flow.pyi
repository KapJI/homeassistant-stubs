import voluptuous as vol
from . import initialize_bot as initialize_bot
from .bot import TelegramBotConfigEntry as TelegramBotConfigEntry
from .const import ATTR_PARSER as ATTR_PARSER, BOT_NAME as BOT_NAME, CONF_CHAT_ID as CONF_CHAT_ID, CONF_PROXY_URL as CONF_PROXY_URL, CONF_TRUSTED_NETWORKS as CONF_TRUSTED_NETWORKS, DEFAULT_TRUSTED_NETWORKS as DEFAULT_TRUSTED_NETWORKS, DOMAIN as DOMAIN, ERROR_FIELD as ERROR_FIELD, ERROR_MESSAGE as ERROR_MESSAGE, PARSER_HTML as PARSER_HTML, PARSER_MD as PARSER_MD, PARSER_MD2 as PARSER_MD2, PARSER_PLAIN_TEXT as PARSER_PLAIN_TEXT, PLATFORM_BROADCAST as PLATFORM_BROADCAST, PLATFORM_POLLING as PLATFORM_POLLING, PLATFORM_WEBHOOKS as PLATFORM_WEBHOOKS, SECTION_ADVANCED_SETTINGS as SECTION_ADVANCED_SETTINGS, SUBENTRY_TYPE_ALLOWED_CHAT_IDS as SUBENTRY_TYPE_ALLOWED_CHAT_IDS
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, ConfigSubentryFlow as ConfigSubentryFlow, OptionsFlow as OptionsFlow, SOURCE_RECONFIGURE as SOURCE_RECONFIGURE, SubentryFlowResult as SubentryFlowResult
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_PLATFORM as CONF_PLATFORM, CONF_URL as CONF_URL
from homeassistant.core import callback as callback
from homeassistant.data_entry_flow import section as section
from homeassistant.helpers.network import NoURLAvailableError as NoURLAvailableError, get_url as get_url
from homeassistant.helpers.selector import SelectSelector as SelectSelector, SelectSelectorConfig as SelectSelectorConfig, TextSelector as TextSelector, TextSelectorConfig as TextSelectorConfig, TextSelectorType as TextSelectorType
from telegram import Bot as Bot, ChatFullInfo as ChatFullInfo
from typing import Any

_LOGGER: Incomplete
DESCRIPTION_PLACEHOLDERS: dict[str, str]
STEP_USER_DATA_SCHEMA: vol.Schema
STEP_RECONFIGURE_USER_DATA_SCHEMA: vol.Schema
STEP_REAUTH_DATA_SCHEMA: vol.Schema
STEP_WEBHOOKS_DATA_SCHEMA: vol.Schema
OPTIONS_SCHEMA: vol.Schema

class OptionsFlowHandler(OptionsFlow):
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...

class TelgramBotConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    @staticmethod
    @callback
    def async_get_options_flow(config_entry: TelegramBotConfigEntry) -> OptionsFlowHandler: ...
    @classmethod
    @callback
    def async_get_supported_subentry_types(cls, config_entry: TelegramBotConfigEntry) -> dict[str, type[ConfigSubentryFlow]]: ...
    _bot: Bot | None
    _bot_name: str
    _step_user_data: dict[str, Any]
    def __init__(self) -> None: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def _shutdown_bot(self) -> None: ...
    async def _validate_bot(self, user_input: dict[str, Any], errors: dict[str, str], placeholders: dict[str, str]) -> str: ...
    async def async_step_webhooks(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    def _validate_webhooks(self, user_input: dict[str, Any], errors: dict[str, str], description_placeholders: dict[str, str]) -> None: ...
    async def async_step_reconfigure(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...

class AllowedChatIdsSubEntryFlowHandler(ConfigSubentryFlow):
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> SubentryFlowResult: ...

async def _async_get_chat_name(bot: Bot, chat_id: int) -> str: ...

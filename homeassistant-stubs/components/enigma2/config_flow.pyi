from .const import CONF_DEEP_STANDBY as CONF_DEEP_STANDBY, CONF_SOURCE_BOUQUET as CONF_SOURCE_BOUQUET, CONF_USE_CHANNEL_ICON as CONF_USE_CHANNEL_ICON, DEFAULT_PORT as DEFAULT_PORT, DEFAULT_SSL as DEFAULT_SSL, DEFAULT_VERIFY_SSL as DEFAULT_VERIFY_SSL, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, SOURCE_USER as SOURCE_USER
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, CONF_SSL as CONF_SSL, CONF_USERNAME as CONF_USERNAME, CONF_VERIFY_SSL as CONF_VERIFY_SSL
from homeassistant.helpers import selector as selector
from homeassistant.helpers.aiohttp_client import async_create_clientsession as async_create_clientsession
from homeassistant.helpers.issue_registry import IssueSeverity as IssueSeverity, async_create_issue as async_create_issue
from typing import Any

CONFIG_SCHEMA: Incomplete

class Enigma2ConfigFlowHandler(ConfigFlow, domain=DOMAIN):
    DATA_KEYS: Incomplete
    OPTIONS_KEYS: Incomplete
    async def validate_user_input(self, user_input: dict[str, Any]) -> dict[str, str] | None: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_import(self, user_input: dict[str, Any]) -> ConfigFlowResult: ...

import logging
from .api import SimpleAuth as SimpleAuth
from .const import API_CONSOLE_URL as API_CONSOLE_URL, DEFAULT_TITLE as DEFAULT_TITLE, DOMAIN as DOMAIN, OAUTH_SCOPES as OAUTH_SCOPES
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.config_entries import ConfigFlowResult as ConfigFlowResult, SOURCE_REAUTH as SOURCE_REAUTH, SOURCE_RECONFIGURE as SOURCE_RECONFIGURE
from homeassistant.const import CONF_ACCESS_TOKEN as CONF_ACCESS_TOKEN, CONF_TOKEN as CONF_TOKEN
from homeassistant.helpers import aiohttp_client as aiohttp_client, config_entry_oauth2_flow as config_entry_oauth2_flow
from typing import Any, override

_LOGGER: Incomplete

class OAuth2FlowHandler(config_entry_oauth2_flow.AbstractOAuth2FlowHandler, domain=DOMAIN):
    DOMAIN = DOMAIN
    @property
    @override
    def logger(self) -> logging.Logger: ...
    @property
    @override
    def extra_authorize_data(self) -> dict[str, Any]: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reconfigure(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    @override
    async def async_oauth_create_entry(self, data: dict[str, Any]) -> ConfigFlowResult: ...

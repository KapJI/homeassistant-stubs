import logging
from .auth import DropboxConfigFlowAuth as DropboxConfigFlowAuth
from .const import DOMAIN as DOMAIN, OAUTH2_SCOPES as OAUTH2_SCOPES
from collections.abc import Mapping
from homeassistant.config_entries import ConfigFlowResult as ConfigFlowResult, SOURCE_REAUTH as SOURCE_REAUTH
from homeassistant.const import CONF_ACCESS_TOKEN as CONF_ACCESS_TOKEN, CONF_TOKEN as CONF_TOKEN
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.config_entry_oauth2_flow import AbstractOAuth2FlowHandler as AbstractOAuth2FlowHandler
from typing import Any, override

class DropboxConfigFlow(AbstractOAuth2FlowHandler, domain=DOMAIN):
    DOMAIN = DOMAIN
    @property
    @override
    def logger(self) -> logging.Logger: ...
    @property
    @override
    def extra_authorize_data(self) -> dict: ...
    @override
    async def async_oauth_create_entry(self, data: dict[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reauth_permissions(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...

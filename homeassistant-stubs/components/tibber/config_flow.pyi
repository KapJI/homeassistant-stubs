import logging
from .const import CONF_LEGACY_ACCESS_TOKEN as CONF_LEGACY_ACCESS_TOKEN, DATA_API_DEFAULT_SCOPES as DATA_API_DEFAULT_SCOPES, DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.config_entries import ConfigFlowResult as ConfigFlowResult, SOURCE_REAUTH as SOURCE_REAUTH, SOURCE_USER as SOURCE_USER
from homeassistant.const import CONF_ACCESS_TOKEN as CONF_ACCESS_TOKEN, CONF_TOKEN as CONF_TOKEN
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.config_entry_oauth2_flow import AbstractOAuth2FlowHandler as AbstractOAuth2FlowHandler
from typing import Any

DATA_SCHEMA: Incomplete
ERR_TIMEOUT: str
ERR_CLIENT: str
ERR_TOKEN: str
TOKEN_URL: str
_LOGGER: Incomplete

class TibberConfigFlow(AbstractOAuth2FlowHandler, domain=DOMAIN):
    VERSION: int
    DOMAIN = DOMAIN
    _access_token: str | None
    _title: str
    def __init__(self) -> None: ...
    @property
    def logger(self) -> logging.Logger: ...
    @property
    def extra_authorize_data(self) -> dict[str, Any]: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_oauth_create_entry(self, data: dict) -> ConfigFlowResult: ...

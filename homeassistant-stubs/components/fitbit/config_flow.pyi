import logging
from . import api as api
from .const import DOMAIN as DOMAIN, OAUTH_SCOPES as OAUTH_SCOPES
from .exceptions import FitbitApiException as FitbitApiException, FitbitAuthException as FitbitAuthException
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_TOKEN as CONF_TOKEN
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers import config_entry_oauth2_flow as config_entry_oauth2_flow
from typing import Any

_LOGGER: Incomplete

class OAuth2FlowHandler(config_entry_oauth2_flow.AbstractOAuth2FlowHandler, domain=DOMAIN):
    DOMAIN = DOMAIN
    reauth_entry: ConfigEntry | None
    @property
    def logger(self) -> logging.Logger: ...
    @property
    def extra_authorize_data(self) -> dict[str, str]: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> FlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def async_oauth_create_entry(self, data: dict[str, Any]) -> FlowResult: ...
    async def async_step_import(self, data: dict[str, Any]) -> FlowResult: ...

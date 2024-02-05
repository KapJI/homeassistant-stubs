import logging
from .const import CONF_LANGUAGE_CODE as CONF_LANGUAGE_CODE, DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN, SUPPORTED_LANGUAGE_CODES as SUPPORTED_LANGUAGE_CODES
from .helpers import default_language_code as default_language_code
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant import config_entries as config_entries
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import callback as callback
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
    def extra_authorize_data(self) -> dict[str, Any]: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> FlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = None) -> FlowResult: ...
    async def async_oauth_create_entry(self, data: dict[str, Any]) -> FlowResult: ...
    @staticmethod
    def async_get_options_flow(config_entry: config_entries.ConfigEntry) -> config_entries.OptionsFlow: ...

class OptionsFlowHandler(config_entries.OptionsFlow):
    config_entry: Incomplete
    def __init__(self, config_entry: config_entries.ConfigEntry) -> None: ...
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> FlowResult: ...

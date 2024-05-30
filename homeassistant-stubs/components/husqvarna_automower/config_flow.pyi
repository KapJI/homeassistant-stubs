import logging
from .const import DOMAIN as DOMAIN, NAME as NAME
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_ACCESS_TOKEN as CONF_ACCESS_TOKEN, CONF_TOKEN as CONF_TOKEN
from homeassistant.helpers import config_entry_oauth2_flow as config_entry_oauth2_flow
from typing import Any

_LOGGER: Incomplete
CONF_USER_ID: str
HUSQVARNA_DEV_PORTAL_URL: str

class HusqvarnaConfigFlowHandler(config_entry_oauth2_flow.AbstractOAuth2FlowHandler, domain=DOMAIN):
    VERSION: int
    DOMAIN = DOMAIN
    reauth_entry: ConfigEntry | None
    async def async_oauth_create_entry(self, data: dict[str, Any]) -> ConfigFlowResult: ...
    @property
    def logger(self) -> logging.Logger: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_missing_scope(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...

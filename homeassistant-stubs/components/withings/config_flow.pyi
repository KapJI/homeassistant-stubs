import logging
from .const import CONF_USE_WEBHOOK as CONF_USE_WEBHOOK, DEFAULT_TITLE as DEFAULT_TITLE, DOMAIN as DOMAIN
from collections.abc import Mapping
from homeassistant.components.webhook import async_generate_id as async_generate_id
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_TOKEN as CONF_TOKEN, CONF_WEBHOOK_ID as CONF_WEBHOOK_ID
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers import config_entry_oauth2_flow as config_entry_oauth2_flow
from typing import Any

class WithingsFlowHandler(config_entry_oauth2_flow.AbstractOAuth2FlowHandler, domain=DOMAIN):
    DOMAIN = DOMAIN
    reauth_entry: ConfigEntry | None
    @property
    def logger(self) -> logging.Logger: ...
    @property
    def extra_authorize_data(self) -> dict[str, str]: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> FlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def async_oauth_create_entry(self, data: dict[str, Any]) -> FlowResult: ...

import logging
from .const import DOMAIN as DOMAIN
from homeassistant.config_entries import ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_TOKEN as CONF_TOKEN
from homeassistant.helpers import config_entry_oauth2_flow as config_entry_oauth2_flow
from typing import Any

class MonzoFlowHandler(config_entry_oauth2_flow.AbstractOAuth2FlowHandler, domain=DOMAIN):
    DOMAIN = DOMAIN
    oauth_data: dict[str, Any]
    @property
    def logger(self) -> logging.Logger: ...
    async def async_step_await_approval_confirmation(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_oauth_create_entry(self, data: dict[str, Any]) -> ConfigFlowResult: ...

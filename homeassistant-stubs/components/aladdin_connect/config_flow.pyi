import logging
from .const import CONFIG_FLOW_MINOR_VERSION as CONFIG_FLOW_MINOR_VERSION, CONFIG_FLOW_VERSION as CONFIG_FLOW_VERSION, DOMAIN as DOMAIN
from collections.abc import Mapping
from homeassistant.config_entries import ConfigFlowResult as ConfigFlowResult, SOURCE_REAUTH as SOURCE_REAUTH
from homeassistant.helpers import config_entry_oauth2_flow as config_entry_oauth2_flow
from typing import Any

class OAuth2FlowHandler(config_entry_oauth2_flow.AbstractOAuth2FlowHandler, domain=DOMAIN):
    DOMAIN = DOMAIN
    VERSION = CONFIG_FLOW_VERSION
    MINOR_VERSION = CONFIG_FLOW_MINOR_VERSION
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reauth(self, user_input: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: Mapping[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_oauth_create_entry(self, data: dict) -> ConfigFlowResult: ...
    @property
    def logger(self) -> logging.Logger: ...

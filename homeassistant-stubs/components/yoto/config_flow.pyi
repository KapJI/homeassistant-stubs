import logging
from .const import DOMAIN as DOMAIN, YOTO_AUDIENCE as YOTO_AUDIENCE, YOTO_SCOPES as YOTO_SCOPES, _LOGGER as _LOGGER
from collections.abc import Mapping
from homeassistant.config_entries import ConfigFlowResult as ConfigFlowResult, SOURCE_REAUTH as SOURCE_REAUTH
from homeassistant.helpers import config_entry_oauth2_flow as config_entry_oauth2_flow
from typing import Any, override

class YotoOAuth2FlowHandler(config_entry_oauth2_flow.AbstractOAuth2FlowHandler, domain=DOMAIN):
    DOMAIN = DOMAIN
    @property
    @override
    def logger(self) -> logging.Logger: ...
    @property
    @override
    def extra_authorize_data(self) -> dict[str, Any]: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    @override
    async def async_oauth_create_entry(self, data: dict[str, Any]) -> ConfigFlowResult: ...

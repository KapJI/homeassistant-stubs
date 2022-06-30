import logging
from .const import NEATO_DOMAIN as NEATO_DOMAIN
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.config_entries import SOURCE_REAUTH as SOURCE_REAUTH
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers import config_entry_oauth2_flow as config_entry_oauth2_flow
from typing import Any

class OAuth2FlowHandler(config_entry_oauth2_flow.AbstractOAuth2FlowHandler):
    DOMAIN: Incomplete
    @property
    def logger(self) -> logging.Logger: ...
    async def async_step_user(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> FlowResult: ...
    async def async_step_reauth_confirm(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_oauth_create_entry(self, data: dict[str, Any]) -> FlowResult: ...

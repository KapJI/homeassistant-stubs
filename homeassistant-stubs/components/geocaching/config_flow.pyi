import logging
from .const import DOMAIN as DOMAIN, ENVIRONMENT as ENVIRONMENT
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.config_entry_oauth2_flow import AbstractOAuth2FlowHandler as AbstractOAuth2FlowHandler
from typing import Any

class GeocachingFlowHandler(AbstractOAuth2FlowHandler):
    DOMAIN: Incomplete
    VERSION: int
    @property
    def logger(self) -> logging.Logger: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> FlowResult: ...
    async def async_step_reauth_confirm(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_oauth_create_entry(self, data: dict[str, Any]) -> FlowResult: ...

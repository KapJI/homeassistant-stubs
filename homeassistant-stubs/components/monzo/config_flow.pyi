import asyncio
import logging
from .api import MonzoAPI as MonzoAPI
from .const import DOMAIN as DOMAIN
from collections.abc import Mapping
from homeassistant.config_entries import ConfigFlowResult as ConfigFlowResult, SOURCE_REAUTH as SOURCE_REAUTH
from homeassistant.const import CONF_TOKEN as CONF_TOKEN
from homeassistant.helpers import config_entry_oauth2_flow as config_entry_oauth2_flow
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from typing import Any, override

APPROVAL_POLL_INTERVAL: int
APPROVAL_TIMEOUT: int

class MonzoFlowHandler(config_entry_oauth2_flow.AbstractOAuth2FlowHandler, domain=DOMAIN):
    DOMAIN = DOMAIN
    VERSION: int
    MINOR_VERSION: int
    oauth_data: dict[str, Any]
    approval_task: asyncio.Task[None] | None
    @property
    @override
    def logger(self) -> logging.Logger: ...
    async def _async_wait_for_approval(self) -> None: ...
    async def async_step_wait_for_approval(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_approval_timeout(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_connection_error(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_finish_approval(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    @override
    async def async_oauth_create_entry(self, data: dict[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...

import logging
from .const import DOMAIN as DOMAIN, SCOPE_VALUES as SCOPE_VALUES
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers import config_entry_oauth2_flow as config_entry_oauth2_flow
from typing import Any

class ElectricKiwiOauth2FlowHandler(config_entry_oauth2_flow.AbstractOAuth2FlowHandler, domain=DOMAIN):
    DOMAIN = DOMAIN
    _reauth_entry: Incomplete
    def __init__(self) -> None: ...
    @property
    def logger(self) -> logging.Logger: ...
    @property
    def extra_authorize_data(self) -> dict[str, Any]: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> FlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def async_oauth_create_entry(self, data: dict) -> FlowResult: ...

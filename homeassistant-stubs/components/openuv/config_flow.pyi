import voluptuous as vol
from .const import CONF_FROM_WINDOW as CONF_FROM_WINDOW, CONF_TO_WINDOW as CONF_TO_WINDOW, DEFAULT_FROM_WINDOW as DEFAULT_FROM_WINDOW, DEFAULT_TO_WINDOW as DEFAULT_TO_WINDOW, DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant import config_entries as config_entries
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_ELEVATION as CONF_ELEVATION, CONF_LATITUDE as CONF_LATITUDE, CONF_LONGITUDE as CONF_LONGITUDE
from homeassistant.core import callback as callback
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers import aiohttp_client as aiohttp_client
from homeassistant.helpers.schema_config_entry_flow import SchemaFlowFormStep as SchemaFlowFormStep, SchemaOptionsFlowHandler as SchemaOptionsFlowHandler
from typing import Any

STEP_REAUTH_SCHEMA: Incomplete
OPTIONS_SCHEMA: Incomplete
OPTIONS_FLOW: Incomplete

class OpenUvData:
    api_key: str
    latitude: float
    longitude: float
    elevation: float
    @property
    def unique_id(self) -> str: ...
    def __init__(self, api_key, latitude, longitude, elevation) -> None: ...

class OpenUvFlowHandler(config_entries.ConfigFlow):
    VERSION: int
    _reauth_data: Incomplete
    def __init__(self) -> None: ...
    @property
    def step_user_schema(self) -> vol.Schema: ...
    async def _async_verify(self, data: OpenUvData, error_step_id: str, error_schema: vol.Schema) -> FlowResult: ...
    @staticmethod
    def async_get_options_flow(config_entry: ConfigEntry) -> SchemaOptionsFlowHandler: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> FlowResult: ...
    async def async_step_reauth_confirm(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_user(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...

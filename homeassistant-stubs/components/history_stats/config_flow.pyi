import voluptuous as vol
from .const import CONF_DURATION as CONF_DURATION, CONF_END as CONF_END, CONF_PERIOD_KEYS as CONF_PERIOD_KEYS, CONF_START as CONF_START, CONF_TYPE_KEYS as CONF_TYPE_KEYS, CONF_TYPE_TIME as CONF_TYPE_TIME, DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN
from .coordinator import HistoryStatsUpdateCoordinator as HistoryStatsUpdateCoordinator
from .data import HistoryStats as HistoryStats
from .sensor import HistoryStatsSensor as HistoryStatsSensor
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.components import websocket_api as websocket_api
from homeassistant.const import CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_NAME as CONF_NAME, CONF_STATE as CONF_STATE, CONF_TYPE as CONF_TYPE
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.schema_config_entry_flow import SchemaCommonFlowHandler as SchemaCommonFlowHandler, SchemaConfigFlowHandler as SchemaConfigFlowHandler, SchemaFlowError as SchemaFlowError, SchemaFlowFormStep as SchemaFlowFormStep
from homeassistant.helpers.selector import DurationSelector as DurationSelector, DurationSelectorConfig as DurationSelectorConfig, EntitySelector as EntitySelector, EntitySelectorConfig as EntitySelectorConfig, SelectSelector as SelectSelector, SelectSelectorConfig as SelectSelectorConfig, SelectSelectorMode as SelectSelectorMode, StateSelector as StateSelector, StateSelectorConfig as StateSelectorConfig, TemplateSelector as TemplateSelector, TextSelector as TextSelector
from homeassistant.helpers.template import Template as Template
from typing import Any

def _validate_two_period_keys(user_input: dict[str, Any]) -> None: ...
async def validate_options(handler: SchemaCommonFlowHandler, user_input: dict[str, Any]) -> dict[str, Any]: ...

DATA_SCHEMA_SETUP: Incomplete

async def get_state_schema(handler: SchemaCommonFlowHandler) -> vol.Schema: ...
async def get_options_schema(handler: SchemaCommonFlowHandler) -> vol.Schema: ...
def _get_options_schema_with_entity_id(entity_id: str) -> vol.Schema: ...

CONFIG_FLOW: Incomplete
OPTIONS_FLOW: Incomplete

class HistoryStatsConfigFlowHandler(SchemaConfigFlowHandler, domain=DOMAIN):
    MINOR_VERSION: int
    config_flow = CONFIG_FLOW
    options_flow = OPTIONS_FLOW
    options_flow_reloads: bool
    def async_config_entry_title(self, options: Mapping[str, Any]) -> str: ...
    @staticmethod
    async def async_setup_preview(hass: HomeAssistant) -> None: ...

@websocket_api.async_response
async def ws_start_preview(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...

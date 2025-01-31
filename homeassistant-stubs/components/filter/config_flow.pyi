from .const import CONF_FILTER_LOWER_BOUND as CONF_FILTER_LOWER_BOUND, CONF_FILTER_NAME as CONF_FILTER_NAME, CONF_FILTER_PRECISION as CONF_FILTER_PRECISION, CONF_FILTER_RADIUS as CONF_FILTER_RADIUS, CONF_FILTER_TIME_CONSTANT as CONF_FILTER_TIME_CONSTANT, CONF_FILTER_UPPER_BOUND as CONF_FILTER_UPPER_BOUND, CONF_FILTER_WINDOW_SIZE as CONF_FILTER_WINDOW_SIZE, CONF_TIME_SMA_TYPE as CONF_TIME_SMA_TYPE, DEFAULT_FILTER_RADIUS as DEFAULT_FILTER_RADIUS, DEFAULT_FILTER_TIME_CONSTANT as DEFAULT_FILTER_TIME_CONSTANT, DEFAULT_NAME as DEFAULT_NAME, DEFAULT_PRECISION as DEFAULT_PRECISION, DEFAULT_WINDOW_SIZE as DEFAULT_WINDOW_SIZE, DOMAIN as DOMAIN, FILTER_NAME_LOWPASS as FILTER_NAME_LOWPASS, FILTER_NAME_OUTLIER as FILTER_NAME_OUTLIER, FILTER_NAME_RANGE as FILTER_NAME_RANGE, FILTER_NAME_THROTTLE as FILTER_NAME_THROTTLE, FILTER_NAME_TIME_SMA as FILTER_NAME_TIME_SMA, FILTER_NAME_TIME_THROTTLE as FILTER_NAME_TIME_THROTTLE, TIME_SMA_LAST as TIME_SMA_LAST
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.const import CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_NAME as CONF_NAME
from homeassistant.helpers.schema_config_entry_flow import SchemaCommonFlowHandler as SchemaCommonFlowHandler, SchemaConfigFlowHandler as SchemaConfigFlowHandler, SchemaFlowFormStep as SchemaFlowFormStep
from homeassistant.helpers.selector import DurationSelector as DurationSelector, DurationSelectorConfig as DurationSelectorConfig, EntitySelector as EntitySelector, EntitySelectorConfig as EntitySelectorConfig, NumberSelector as NumberSelector, NumberSelectorConfig as NumberSelectorConfig, NumberSelectorMode as NumberSelectorMode, SelectSelector as SelectSelector, SelectSelectorConfig as SelectSelectorConfig, SelectSelectorMode as SelectSelectorMode, TextSelector as TextSelector
from typing import Any

FILTERS: Incomplete

async def get_next_step(user_input: dict[str, Any]) -> str: ...
async def validate_options(handler: SchemaCommonFlowHandler, user_input: dict[str, Any]) -> dict[str, Any]: ...

DATA_SCHEMA_SETUP: Incomplete
BASE_OPTIONS_SCHEMA: Incomplete
OUTLIER_SCHEMA: Incomplete
LOWPASS_SCHEMA: Incomplete
RANGE_SCHEMA: Incomplete
TIME_SMA_SCHEMA: Incomplete
THROTTLE_SCHEMA: Incomplete
TIME_THROTTLE_SCHEMA: Incomplete
CONFIG_FLOW: Incomplete
OPTIONS_FLOW: Incomplete

class FilterConfigFlowHandler(SchemaConfigFlowHandler, domain=DOMAIN):
    config_flow = CONFIG_FLOW
    options_flow = OPTIONS_FLOW
    def async_config_entry_title(self, options: Mapping[str, Any]) -> str: ...

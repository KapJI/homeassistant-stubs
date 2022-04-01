from .const import CONF_ROUND_DIGITS as CONF_ROUND_DIGITS, CONF_SOURCE_SENSOR as CONF_SOURCE_SENSOR, CONF_UNIT_PREFIX as CONF_UNIT_PREFIX, CONF_UNIT_TIME as CONF_UNIT_TIME, DOMAIN as DOMAIN, METHOD_LEFT as METHOD_LEFT, METHOD_RIGHT as METHOD_RIGHT, METHOD_TRAPEZOIDAL as METHOD_TRAPEZOIDAL
from collections.abc import Mapping
from homeassistant.const import CONF_METHOD as CONF_METHOD, CONF_NAME as CONF_NAME, CONF_UNIT_OF_MEASUREMENT as CONF_UNIT_OF_MEASUREMENT, TIME_DAYS as TIME_DAYS, TIME_HOURS as TIME_HOURS, TIME_MINUTES as TIME_MINUTES, TIME_SECONDS as TIME_SECONDS
from homeassistant.helpers import selector as selector
from homeassistant.helpers.schema_config_entry_flow import SchemaConfigFlowHandler as SchemaConfigFlowHandler, SchemaFlowFormStep as SchemaFlowFormStep, SchemaFlowMenuStep as SchemaFlowMenuStep
from typing import Any

UNIT_PREFIXES: Any
TIME_UNITS: Any
INTEGRATION_METHODS: Any
OPTIONS_SCHEMA: Any
CONFIG_SCHEMA: Any
CONFIG_FLOW: dict[str, Union[SchemaFlowFormStep, SchemaFlowMenuStep]]
OPTIONS_FLOW: dict[str, Union[SchemaFlowFormStep, SchemaFlowMenuStep]]

class ConfigFlowHandler(SchemaConfigFlowHandler):
    config_flow: Any
    options_flow: Any
    def async_config_entry_title(self, options: Mapping[str, Any]) -> str: ...

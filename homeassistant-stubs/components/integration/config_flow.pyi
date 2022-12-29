from .const import CONF_ROUND_DIGITS as CONF_ROUND_DIGITS, CONF_SOURCE_SENSOR as CONF_SOURCE_SENSOR, CONF_UNIT_PREFIX as CONF_UNIT_PREFIX, CONF_UNIT_TIME as CONF_UNIT_TIME, DOMAIN as DOMAIN, METHOD_LEFT as METHOD_LEFT, METHOD_RIGHT as METHOD_RIGHT, METHOD_TRAPEZOIDAL as METHOD_TRAPEZOIDAL
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.const import CONF_METHOD as CONF_METHOD, CONF_NAME as CONF_NAME, UnitOfTime as UnitOfTime
from homeassistant.helpers import selector as selector
from homeassistant.helpers.schema_config_entry_flow import SchemaConfigFlowHandler as SchemaConfigFlowHandler, SchemaFlowFormStep as SchemaFlowFormStep
from typing import Any

UNIT_PREFIXES: Incomplete
TIME_UNITS: Incomplete
INTEGRATION_METHODS: Incomplete
OPTIONS_SCHEMA: Incomplete
CONFIG_SCHEMA: Incomplete
CONFIG_FLOW: Incomplete
OPTIONS_FLOW: Incomplete

class ConfigFlowHandler(SchemaConfigFlowHandler):
    config_flow: Incomplete
    options_flow: Incomplete
    def async_config_entry_title(self, options: Mapping[str, Any]) -> str: ...

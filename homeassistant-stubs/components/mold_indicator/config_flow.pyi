from .const import CONF_CALIBRATION_FACTOR as CONF_CALIBRATION_FACTOR, CONF_INDOOR_HUMIDITY as CONF_INDOOR_HUMIDITY, CONF_INDOOR_TEMP as CONF_INDOOR_TEMP, CONF_OUTDOOR_TEMP as CONF_OUTDOOR_TEMP, DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass
from homeassistant.const import CONF_NAME as CONF_NAME, Platform as Platform
from homeassistant.helpers.schema_config_entry_flow import SchemaCommonFlowHandler as SchemaCommonFlowHandler, SchemaConfigFlowHandler as SchemaConfigFlowHandler, SchemaFlowError as SchemaFlowError, SchemaFlowFormStep as SchemaFlowFormStep
from homeassistant.helpers.selector import EntitySelector as EntitySelector, EntitySelectorConfig as EntitySelectorConfig, NumberSelector as NumberSelector, NumberSelectorConfig as NumberSelectorConfig, NumberSelectorMode as NumberSelectorMode, TextSelector as TextSelector
from typing import Any

async def validate_input(handler: SchemaCommonFlowHandler, user_input: dict[str, Any]) -> dict[str, Any]: ...

DATA_SCHEMA_OPTIONS: Incomplete
DATA_SCHEMA_CONFIG: Incomplete
CONFIG_FLOW: Incomplete
OPTIONS_FLOW: Incomplete

class MoldIndicatorConfigFlowHandler(SchemaConfigFlowHandler, domain=DOMAIN):
    config_flow = CONFIG_FLOW
    options_flow = OPTIONS_FLOW
    def async_config_entry_title(self, options: Mapping[str, Any]) -> str: ...

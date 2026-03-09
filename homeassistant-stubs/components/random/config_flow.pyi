import voluptuous as vol
from .const import DOMAIN as DOMAIN
from .sensor import DEFAULT_MAX as DEFAULT_MAX, DEFAULT_MIN as DEFAULT_MIN
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine, Mapping
from enum import StrEnum
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass
from homeassistant.components.sensor import DEVICE_CLASS_UNITS as DEVICE_CLASS_UNITS, SensorDeviceClass as SensorDeviceClass
from homeassistant.const import CONF_DEVICE_CLASS as CONF_DEVICE_CLASS, CONF_MAXIMUM as CONF_MAXIMUM, CONF_MINIMUM as CONF_MINIMUM, CONF_NAME as CONF_NAME, CONF_UNIT_OF_MEASUREMENT as CONF_UNIT_OF_MEASUREMENT, Platform as Platform
from homeassistant.core import callback as callback
from homeassistant.helpers.schema_config_entry_flow import SchemaCommonFlowHandler as SchemaCommonFlowHandler, SchemaConfigFlowHandler as SchemaConfigFlowHandler, SchemaFlowFormStep as SchemaFlowFormStep, SchemaFlowMenuStep as SchemaFlowMenuStep
from homeassistant.helpers.selector import SelectSelector as SelectSelector, SelectSelectorConfig as SelectSelectorConfig, SelectSelectorMode as SelectSelectorMode, TextSelector as TextSelector
from typing import Any

class _FlowType(StrEnum):
    CONFIG = 'config'
    OPTION = 'option'

def _generate_schema(domain: str, flow_type: _FlowType) -> vol.Schema: ...
async def choose_options_step(options: dict[str, Any]) -> str: ...
def _validate_unit(options: dict[str, Any]) -> None: ...
def validate_user_input(entity_type: str) -> Callable[[SchemaCommonFlowHandler, dict[str, Any]], Coroutine[Any, Any, dict[str, Any]]]: ...

RANDOM_TYPES: Incomplete
CONFIG_FLOW: Incomplete
OPTIONS_FLOW: Incomplete

class RandomConfigFlowHandler(SchemaConfigFlowHandler, domain=DOMAIN):
    config_flow = CONFIG_FLOW
    options_flow = OPTIONS_FLOW
    options_flow_reloads: bool
    @callback
    def async_config_entry_title(self, options: Mapping[str, Any]) -> str: ...

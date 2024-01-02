import voluptuous as vol
from .const import CONF_PROCESS as CONF_PROCESS, DOMAIN as DOMAIN
from .util import get_all_running_processes as get_all_running_processes
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.core import callback as callback
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers.issue_registry import IssueSeverity as IssueSeverity, async_create_issue as async_create_issue
from homeassistant.helpers.schema_config_entry_flow import SchemaCommonFlowHandler as SchemaCommonFlowHandler, SchemaConfigFlowHandler as SchemaConfigFlowHandler, SchemaFlowFormStep as SchemaFlowFormStep
from homeassistant.helpers.selector import SelectSelector as SelectSelector, SelectSelectorConfig as SelectSelectorConfig, SelectSelectorMode as SelectSelectorMode
from homeassistant.util import slugify as slugify
from typing import Any

async def validate_sensor_setup(handler: SchemaCommonFlowHandler, user_input: dict[str, Any]) -> dict[str, Any]: ...
async def validate_import_sensor_setup(handler: SchemaCommonFlowHandler, user_input: dict[str, Any]) -> dict[str, Any]: ...
async def get_sensor_setup_schema(handler: SchemaCommonFlowHandler) -> vol.Schema: ...
async def get_suggested_value(handler: SchemaCommonFlowHandler) -> dict[str, Any]: ...

CONFIG_FLOW: Incomplete
OPTIONS_FLOW: Incomplete

class SystemMonitorConfigFlowHandler(SchemaConfigFlowHandler, domain=DOMAIN):
    config_flow = CONFIG_FLOW
    options_flow = OPTIONS_FLOW
    def async_config_entry_title(self, options: Mapping[str, Any]) -> str: ...
    def async_create_entry(self, data: Mapping[str, Any], **kwargs: Any) -> FlowResult: ...

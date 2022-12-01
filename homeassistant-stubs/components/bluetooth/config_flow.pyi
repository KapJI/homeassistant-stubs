from . import models as models
from .const import CONF_ADAPTER as CONF_ADAPTER, CONF_DETAILS as CONF_DETAILS, CONF_PASSIVE as CONF_PASSIVE, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components import onboarding as onboarding
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow
from homeassistant.core import callback as callback
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers.schema_config_entry_flow import SchemaFlowFormStep as SchemaFlowFormStep, SchemaOptionsFlowHandler as SchemaOptionsFlowHandler
from homeassistant.helpers.typing import DiscoveryInfoType as DiscoveryInfoType
from typing import Any

OPTIONS_SCHEMA: Incomplete
OPTIONS_FLOW: Incomplete

class BluetoothConfigFlow(ConfigFlow):
    VERSION: int
    _adapter: Incomplete
    _details: Incomplete
    _adapters: Incomplete
    def __init__(self) -> None: ...
    async def async_step_integration_discovery(self, discovery_info: DiscoveryInfoType) -> FlowResult: ...
    async def async_step_single_adapter(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_multiple_adapters(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_user(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    @staticmethod
    def async_get_options_flow(config_entry: ConfigEntry) -> SchemaOptionsFlowHandler: ...
    @classmethod
    def async_supports_options_flow(cls, config_entry: ConfigEntry) -> bool: ...

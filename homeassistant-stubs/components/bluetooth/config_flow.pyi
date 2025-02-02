from .const import CONF_ADAPTER as CONF_ADAPTER, CONF_DETAILS as CONF_DETAILS, CONF_PASSIVE as CONF_PASSIVE, CONF_SOURCE as CONF_SOURCE, CONF_SOURCE_CONFIG_ENTRY_ID as CONF_SOURCE_CONFIG_ENTRY_ID, CONF_SOURCE_DEVICE_ID as CONF_SOURCE_DEVICE_ID, CONF_SOURCE_DOMAIN as CONF_SOURCE_DOMAIN, CONF_SOURCE_MODEL as CONF_SOURCE_MODEL, DOMAIN as DOMAIN
from .util import adapter_title as adapter_title
from _typeshed import Incomplete
from bluetooth_adapters import AdapterDetails
from homeassistant.components import onboarding as onboarding
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, OptionsFlow as OptionsFlow
from homeassistant.core import callback as callback
from homeassistant.helpers.schema_config_entry_flow import SchemaFlowFormStep as SchemaFlowFormStep, SchemaOptionsFlowHandler as SchemaOptionsFlowHandler
from homeassistant.helpers.typing import DiscoveryInfoType as DiscoveryInfoType
from typing import Any

OPTIONS_SCHEMA: Incomplete
OPTIONS_FLOW: Incomplete

def adapter_display_info(adapter: str, details: AdapterDetails) -> str: ...

class BluetoothConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    _adapter: str | None
    _details: AdapterDetails | None
    _adapters: dict[str, AdapterDetails]
    _placeholders: dict[str, str]
    def __init__(self) -> None: ...
    async def async_step_integration_discovery(self, discovery_info: DiscoveryInfoType) -> ConfigFlowResult: ...
    @callback
    def _async_set_adapter_info(self, adapter: str, details: AdapterDetails) -> None: ...
    async def async_step_single_adapter(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_multiple_adapters(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_external_scanner(self, user_input: dict[str, Any]) -> ConfigFlowResult: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    @staticmethod
    @callback
    def async_get_options_flow(config_entry: ConfigEntry) -> SchemaOptionsFlowHandler | RemoteAdapterOptionsFlowHandler | LocalNoPassiveOptionsFlowHandler: ...
    @classmethod
    @callback
    def async_supports_options_flow(cls, config_entry: ConfigEntry) -> bool: ...

class RemoteAdapterOptionsFlowHandler(OptionsFlow):
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...

class LocalNoPassiveOptionsFlowHandler(OptionsFlow):
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...

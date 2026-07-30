from . import RussoundConfigEntry as RussoundConfigEntry
from .const import CONF_BAUDRATE as CONF_BAUDRATE, CONF_ZONE_SOURCE_EXCLUSION as CONF_ZONE_SOURCE_EXCLUSION, DEFAULT_BAUDRATE as DEFAULT_BAUDRATE, DEFAULT_PORT as DEFAULT_PORT, DOMAIN as DOMAIN, RUSSOUND_RIO_EXCEPTIONS as RUSSOUND_RIO_EXCEPTIONS, TYPE_SERIAL as TYPE_SERIAL, TYPE_TCP as TYPE_TCP
from _typeshed import Incomplete
from aiorussound.connection import RussoundConnectionHandler as RussoundConnectionHandler
from aiorussound.rio import Controller as Controller
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, OptionsFlowWithReload as OptionsFlowWithReload, SOURCE_RECONFIGURE as SOURCE_RECONFIGURE
from homeassistant.const import CONF_DEVICE as CONF_DEVICE, CONF_HOST as CONF_HOST, CONF_NAME as CONF_NAME, CONF_PORT as CONF_PORT, CONF_TYPE as CONF_TYPE
from homeassistant.core import callback as callback
from homeassistant.helpers.selector import SelectSelector as SelectSelector, SelectSelectorConfig as SelectSelectorConfig, SerialPortSelector as SerialPortSelector
from homeassistant.helpers.service_info.zeroconf import ZeroconfServiceInfo as ZeroconfServiceInfo
from typing import Any, override

TRANSPORT_SCHEMA: Incomplete
TCP_SCHEMA: Incomplete
SERIAL_SCHEMA: Incomplete
OPTIONS_SCHEMA: Incomplete
_LOGGER: Incomplete

async def _async_validate_connection(connection_handler: RussoundConnectionHandler) -> Controller | None: ...

class OptionsFlowHandler(OptionsFlowWithReload):
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...

class FlowHandler(ConfigFlow, domain=DOMAIN):
    VERSION: int
    @staticmethod
    @callback
    @override
    def async_get_options_flow(config_entry: RussoundConfigEntry) -> OptionsFlowHandler: ...
    data: dict[str, Any]
    def __init__(self) -> None: ...
    async def _async_finish_manual_setup(self, controller: Controller, data: dict[str, Any]) -> ConfigFlowResult: ...
    @override
    async def async_step_zeroconf(self, discovery_info: ZeroconfServiceInfo) -> ConfigFlowResult: ...
    async def async_step_discovery_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    @override
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_tcp(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_serial(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reconfigure(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...

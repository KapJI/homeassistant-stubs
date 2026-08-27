import voluptuous as vol
from . import create_modbus_params as create_modbus_params
from .const import CONF_BAUDRATE as CONF_BAUDRATE, CONF_UNIT as CONF_UNIT, DEFAULT_BAUDRATE as DEFAULT_BAUDRATE, DEFAULT_PORT as DEFAULT_PORT, DOMAIN as DOMAIN, TYPE_SERIAL as TYPE_SERIAL, TYPE_TCP as TYPE_TCP
from _typeshed import Incomplete
from homeassistant.components.modbus import async_get_temporary_unit as async_get_temporary_unit
from homeassistant.config_entries import ConfigEntryState as ConfigEntryState, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_DEVICE as CONF_DEVICE, CONF_HOST as CONF_HOST, CONF_PORT as CONF_PORT, CONF_TYPE as CONF_TYPE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.selector import NumberSelector as NumberSelector, NumberSelectorConfig as NumberSelectorConfig, NumberSelectorMode as NumberSelectorMode, SerialPortSelector as SerialPortSelector, TextSelector as TextSelector
from typing import Any, override

_LOGGER: Incomplete
UNIT_SELECTOR: Incomplete
STEP_TCP_DATA_SCHEMA: Incomplete
STEP_SERIAL_DATA_SCHEMA: Incomplete

async def check_connection(hass: HomeAssistant, data: dict[str, Any]) -> str | None: ...

class FlexitConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    @override
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_tcp(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_serial(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def _async_step_connection(self, connection_type: str, schema: vol.Schema, user_input: dict[str, Any] | None) -> ConfigFlowResult: ...
    async def async_step_reconfigure(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...

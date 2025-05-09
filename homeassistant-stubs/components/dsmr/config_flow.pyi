from .const import CONF_DSMR_VERSION as CONF_DSMR_VERSION, CONF_SERIAL_ID as CONF_SERIAL_ID, CONF_SERIAL_ID_GAS as CONF_SERIAL_ID_GAS, CONF_TIME_BETWEEN_UPDATE as CONF_TIME_BETWEEN_UPDATE, DEFAULT_TIME_BETWEEN_UPDATE as DEFAULT_TIME_BETWEEN_UPDATE, DOMAIN as DOMAIN, DSMR_PROTOCOL as DSMR_PROTOCOL, DSMR_VERSIONS as DSMR_VERSIONS, LOGGER as LOGGER, RFXTRX_DSMR_PROTOCOL as RFXTRX_DSMR_PROTOCOL
from _typeshed import Incomplete
from dsmr_parser.objects import DSMRObject as DSMRObject
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, OptionsFlow as OptionsFlow
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PORT as CONF_PORT, CONF_PROTOCOL as CONF_PROTOCOL, CONF_TYPE as CONF_TYPE
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from typing import Any

CONF_MANUAL_PATH: str

class DSMRConnection:
    _host: Incomplete
    _port: Incomplete
    _dsmr_version: Incomplete
    _protocol: Incomplete
    _telegram: dict[str, DSMRObject]
    _equipment_identifier: Incomplete
    def __init__(self, host: str | None, port: int, dsmr_version: str, protocol: str) -> None: ...
    def equipment_identifier(self) -> str | None: ...
    def equipment_identifier_gas(self) -> str | None: ...
    async def validate_connect(self, hass: HomeAssistant) -> bool: ...

async def _validate_dsmr_connection(hass: HomeAssistant, data: dict[str, Any], protocol: str) -> dict[str, str | None]: ...

class DSMRFlowHandler(ConfigFlow, domain=DOMAIN):
    VERSION: int
    _dsmr_version: str | None
    @staticmethod
    @callback
    def async_get_options_flow(config_entry: ConfigEntry) -> DSMROptionFlowHandler: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_setup_network(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_setup_serial(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_setup_serial_manual_path(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_validate_dsmr(self, input_data: dict[str, Any], errors: dict[str, str]) -> dict[str, Any]: ...

class DSMROptionFlowHandler(OptionsFlow):
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...

def get_serial_by_id(dev_path: str) -> str: ...

class CannotConnect(HomeAssistantError): ...
class CannotCommunicate(HomeAssistantError): ...

from .const import CONF_DSMR_VERSION as CONF_DSMR_VERSION, CONF_ENCRYPTION_KEY as CONF_ENCRYPTION_KEY, CONF_SERIAL_ID as CONF_SERIAL_ID, CONF_SERIAL_ID_GAS as CONF_SERIAL_ID_GAS, CONF_TIME_BETWEEN_UPDATE as CONF_TIME_BETWEEN_UPDATE, DEFAULT_TIME_BETWEEN_UPDATE as DEFAULT_TIME_BETWEEN_UPDATE, DOMAIN as DOMAIN, DSMR_PROTOCOL as DSMR_PROTOCOL, DSMR_VERSIONS as DSMR_VERSIONS, DSMR_VERSIONS_WITHOUT_EQUIPMENT_ID as DSMR_VERSIONS_WITHOUT_EQUIPMENT_ID, ENCRYPTED_DSMR_VERSIONS as ENCRYPTED_DSMR_VERSIONS, LOGGER as LOGGER, RFXTRX_DSMR_PROTOCOL as RFXTRX_DSMR_PROTOCOL
from _typeshed import Incomplete
from dsmr_parser.objects import DSMRObject as DSMRObject
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, OptionsFlow as OptionsFlow
from homeassistant.const import CONF_PORT as CONF_PORT, CONF_PROTOCOL as CONF_PROTOCOL
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.selector import SerialPortSelector as SerialPortSelector
from typing import Any, override

ENCRYPTION_KEY_PATTERN: Incomplete

class DSMRConnection:
    _port: Incomplete
    _dsmr_version: Incomplete
    _protocol: Incomplete
    _encryption_key: Incomplete
    _decryption_failed: bool
    _telegram: dict[str, DSMRObject]
    _equipment_identifier: Incomplete
    def __init__(self, port: str, dsmr_version: str, protocol: str, encryption_key: str = '') -> None: ...
    def equipment_identifier(self) -> str | None: ...
    def equipment_identifier_gas(self) -> str | None: ...
    async def validate_connect(self, hass: HomeAssistant) -> bool: ...
    def decryption_failed(self) -> bool: ...

async def _validate_dsmr_connection(hass: HomeAssistant, data: dict[str, Any], protocol: str) -> dict[str, str | None]: ...

class DSMRFlowHandler(ConfigFlow, domain=DOMAIN):
    VERSION: int
    _pending_data: dict[str, Any]
    _pending_title: str
    @staticmethod
    @callback
    @override
    def async_get_options_flow(config_entry: ConfigEntry) -> DSMROptionFlowHandler: ...
    @override
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_encryption_key(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_validate_dsmr(self, input_data: dict[str, Any], errors: dict[str, str]) -> dict[str, Any]: ...

class DSMROptionFlowHandler(OptionsFlow):
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...

class CannotConnect(HomeAssistantError): ...
class CannotCommunicate(HomeAssistantError): ...
class InvalidKey(HomeAssistantError): ...

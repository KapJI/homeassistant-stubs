from .const import ATTR_ADDRESS as ATTR_ADDRESS, ATTR_HUB as ATTR_HUB, ATTR_STATE as ATTR_STATE, ATTR_UNIT as ATTR_UNIT, ATTR_VALUE as ATTR_VALUE, CALL_TYPE_COIL as CALL_TYPE_COIL, CALL_TYPE_DISCRETE as CALL_TYPE_DISCRETE, CALL_TYPE_REGISTER_HOLDING as CALL_TYPE_REGISTER_HOLDING, CALL_TYPE_REGISTER_INPUT as CALL_TYPE_REGISTER_INPUT, CALL_TYPE_WRITE_COIL as CALL_TYPE_WRITE_COIL, CALL_TYPE_WRITE_COILS as CALL_TYPE_WRITE_COILS, CALL_TYPE_WRITE_REGISTER as CALL_TYPE_WRITE_REGISTER, CALL_TYPE_WRITE_REGISTERS as CALL_TYPE_WRITE_REGISTERS, CONF_BAUDRATE as CONF_BAUDRATE, CONF_BYTESIZE as CONF_BYTESIZE, CONF_CLOSE_COMM_ON_ERROR as CONF_CLOSE_COMM_ON_ERROR, CONF_MSG_WAIT as CONF_MSG_WAIT, CONF_PARITY as CONF_PARITY, CONF_RETRIES as CONF_RETRIES, CONF_RETRY_ON_EMPTY as CONF_RETRY_ON_EMPTY, CONF_STOPBITS as CONF_STOPBITS, DEFAULT_HUB as DEFAULT_HUB, PLATFORMS as PLATFORMS, RTUOVERTCP as RTUOVERTCP, SERIAL as SERIAL, SERVICE_RESTART as SERVICE_RESTART, SERVICE_STOP as SERVICE_STOP, SERVICE_WRITE_COIL as SERVICE_WRITE_COIL, SERVICE_WRITE_REGISTER as SERVICE_WRITE_REGISTER, SIGNAL_START_ENTITY as SIGNAL_START_ENTITY, SIGNAL_STOP_ENTITY as SIGNAL_STOP_ENTITY, TCP as TCP, UDP as UDP
from collections.abc import Callable as Callable
from homeassistant.const import CONF_DELAY as CONF_DELAY, CONF_HOST as CONF_HOST, CONF_METHOD as CONF_METHOD, CONF_NAME as CONF_NAME, CONF_PORT as CONF_PORT, CONF_TIMEOUT as CONF_TIMEOUT, CONF_TYPE as CONF_TYPE, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.helpers.discovery import async_load_platform as async_load_platform
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.event import async_call_later as async_call_later
from homeassistant.helpers.typing import ConfigType as ConfigType
from pymodbus.client.sync import BaseModbusClient as BaseModbusClient
from pymodbus.pdu import ModbusResponse as ModbusResponse
from typing import Any, NamedTuple

_LOGGER: Any

class ConfEntry(NamedTuple):
    call_type: Any
    attr: Any
    func_name: Any

class RunEntry(NamedTuple):
    attr: Any
    func: Any
PYMODBUS_CALL: Any

async def async_modbus_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...

class ModbusHub:
    _client: Any
    _async_cancel_listener: Any
    _in_error: bool
    _lock: Any
    hass: Any
    name: Any
    _config_type: Any
    _config_delay: Any
    _pb_call: Any
    _pb_class: Any
    _pb_params: Any
    _msg_wait: Any
    def __init__(self, hass: HomeAssistant, client_config: dict[str, Any]) -> None: ...
    def _log_error(self, text: str, error_state: bool = ...) -> None: ...
    async def async_setup(self) -> bool: ...
    def async_end_delay(self, args: Any) -> None: ...
    async def async_restart(self) -> None: ...
    async def async_close(self) -> None: ...
    def _pymodbus_connect(self) -> bool: ...
    def _pymodbus_call(self, unit: Union[int, None], address: int, value: Union[int, list[int]], use_call: str) -> ModbusResponse: ...
    async def async_pymodbus_call(self, unit: Union[int, None], address: int, value: Union[int, list[int]], use_call: str) -> Union[ModbusResponse, None]: ...

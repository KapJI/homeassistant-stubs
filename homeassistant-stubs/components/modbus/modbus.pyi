import asyncio
from .connection import ModbusEndpoint as ModbusEndpoint
from .const import CALL_TYPE_COIL as CALL_TYPE_COIL, CALL_TYPE_DISCRETE as CALL_TYPE_DISCRETE, CALL_TYPE_REGISTER_HOLDING as CALL_TYPE_REGISTER_HOLDING, CALL_TYPE_REGISTER_INPUT as CALL_TYPE_REGISTER_INPUT, CALL_TYPE_WRITE_COIL as CALL_TYPE_WRITE_COIL, CALL_TYPE_WRITE_COILS as CALL_TYPE_WRITE_COILS, CALL_TYPE_WRITE_REGISTER as CALL_TYPE_WRITE_REGISTER, CALL_TYPE_WRITE_REGISTERS as CALL_TYPE_WRITE_REGISTERS, CONF_BAUDRATE as CONF_BAUDRATE, CONF_BYTESIZE as CONF_BYTESIZE, CONF_DEVICE_ADDRESS as CONF_DEVICE_ADDRESS, CONF_MSG_WAIT as CONF_MSG_WAIT, CONF_PARITY as CONF_PARITY, CONF_STOPBITS as CONF_STOPBITS, DATA_MODBUS_HUBS as DATA_MODBUS_HUBS, DEVICE_ID as DEVICE_ID, DOMAIN as DOMAIN, LOGGER as LOGGER, PLATFORMS as PLATFORMS, RTUOVERTCP as RTUOVERTCP, SERIAL as SERIAL, TCP as TCP, UDP as UDP
from .validators import check_config as check_config
from _typeshed import Incomplete
from homeassistant.const import CONF_DELAY as CONF_DELAY, CONF_HOST as CONF_HOST, CONF_METHOD as CONF_METHOD, CONF_NAME as CONF_NAME, CONF_PORT as CONF_PORT, CONF_SLAVE as CONF_SLAVE, CONF_TIMEOUT as CONF_TIMEOUT, CONF_TYPE as CONF_TYPE, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant
from homeassistant.helpers.discovery import async_load_platform as async_load_platform
from homeassistant.helpers.typing import ConfigType as ConfigType
from pymodbus.client import AsyncModbusSerialClient, AsyncModbusTcpClient, AsyncModbusUdpClient
from pymodbus.pdu import ModbusPDU as ModbusPDU
from typing import Any, NamedTuple

PRIMARY_RECONNECT_DELAY: int

class ConfEntry(NamedTuple):
    call_type: Incomplete
    attr: Incomplete
    func_name: Incomplete
    value_attr_name: Incomplete

class RunEntry(NamedTuple):
    attr: Incomplete
    func: Incomplete
    value_attr_name: Incomplete

PB_CALL: Incomplete

def entity_unit_id(entity_config: dict[str, Any]) -> int: ...
async def async_modbus_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def _async_modbus_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...

class ModbusHub:
    _client: AsyncModbusSerialClient | AsyncModbusTcpClient | AsyncModbusUdpClient | None
    _lock: Incomplete
    event_connected: Incomplete
    hass: Incomplete
    name: Incomplete
    _config_type: Incomplete
    config_delay: Incomplete
    _pb_request: dict[str, RunEntry]
    _connect_task: asyncio.Task
    _last_log_error: str
    _pb_class: Incomplete
    _pb_params: Incomplete
    endpoint: ModbusEndpoint
    _msg_wait: Incomplete
    units: Incomplete
    def __init__(self, hass: HomeAssistant, client_config: dict[str, Any]) -> None: ...
    @property
    def connected(self) -> bool: ...
    def _log_error(self, text: str) -> None: ...
    async def async_pb_connect(self) -> None: ...
    async def async_setup(self) -> bool: ...
    async def async_close(self) -> None: ...
    async def low_level_pb_call(self, slave: int | None, address: int, value: int | list[int], use_call: str) -> ModbusPDU | None: ...
    async def async_pb_call(self, unit: int | None, address: int, value: int | list[int], use_call: str) -> ModbusPDU | None: ...

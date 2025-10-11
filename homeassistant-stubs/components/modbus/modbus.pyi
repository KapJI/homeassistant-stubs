import asyncio
from .const import ATTR_ADDRESS as ATTR_ADDRESS, ATTR_HUB as ATTR_HUB, ATTR_SLAVE as ATTR_SLAVE, ATTR_UNIT as ATTR_UNIT, ATTR_VALUE as ATTR_VALUE, CALL_TYPE_COIL as CALL_TYPE_COIL, CALL_TYPE_DISCRETE as CALL_TYPE_DISCRETE, CALL_TYPE_REGISTER_HOLDING as CALL_TYPE_REGISTER_HOLDING, CALL_TYPE_REGISTER_INPUT as CALL_TYPE_REGISTER_INPUT, CALL_TYPE_WRITE_COIL as CALL_TYPE_WRITE_COIL, CALL_TYPE_WRITE_COILS as CALL_TYPE_WRITE_COILS, CALL_TYPE_WRITE_REGISTER as CALL_TYPE_WRITE_REGISTER, CALL_TYPE_WRITE_REGISTERS as CALL_TYPE_WRITE_REGISTERS, CONF_BAUDRATE as CONF_BAUDRATE, CONF_BYTESIZE as CONF_BYTESIZE, CONF_MSG_WAIT as CONF_MSG_WAIT, CONF_PARITY as CONF_PARITY, CONF_STOPBITS as CONF_STOPBITS, DEFAULT_HUB as DEFAULT_HUB, DEVICE_ID as DEVICE_ID, DOMAIN as DOMAIN, PLATFORMS as PLATFORMS, RTUOVERTCP as RTUOVERTCP, SERIAL as SERIAL, SERVICE_STOP as SERVICE_STOP, SERVICE_WRITE_COIL as SERVICE_WRITE_COIL, SERVICE_WRITE_REGISTER as SERVICE_WRITE_REGISTER, SIGNAL_STOP_ENTITY as SIGNAL_STOP_ENTITY, TCP as TCP, UDP as UDP, _LOGGER as _LOGGER
from .validators import check_config as check_config
from _typeshed import Incomplete
from homeassistant.const import ATTR_STATE as ATTR_STATE, CONF_DELAY as CONF_DELAY, CONF_HOST as CONF_HOST, CONF_METHOD as CONF_METHOD, CONF_NAME as CONF_NAME, CONF_PORT as CONF_PORT, CONF_TIMEOUT as CONF_TIMEOUT, CONF_TYPE as CONF_TYPE, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, ServiceCall as ServiceCall
from homeassistant.helpers.discovery import async_load_platform as async_load_platform
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.util.hass_dict import HassKey as HassKey
from pymodbus.client import AsyncModbusSerialClient, AsyncModbusTcpClient, AsyncModbusUdpClient
from pymodbus.pdu import ModbusPDU as ModbusPDU
from typing import Any, NamedTuple

DATA_MODBUS_HUBS: HassKey[dict[str, ModbusHub]]
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

async def async_modbus_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...

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
    _msg_wait: Incomplete
    def __init__(self, hass: HomeAssistant, client_config: dict[str, Any]) -> None: ...
    def _log_error(self, text: str) -> None: ...
    async def async_pb_connect(self) -> None: ...
    async def async_setup(self) -> bool: ...
    async def async_restart(self) -> None: ...
    async def async_close(self) -> None: ...
    async def low_level_pb_call(self, slave: int | None, address: int, value: int | list[int], use_call: str) -> ModbusPDU | None: ...
    async def async_pb_call(self, unit: int | None, address: int, value: int | list[int], use_call: str) -> ModbusPDU | None: ...

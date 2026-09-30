from .const import CONF_BAUDRATE as CONF_BAUDRATE, DOMAIN as DOMAIN, TYPE_SERIAL as TYPE_SERIAL
from .entity import SolarEdgeModbusEntity as SolarEdgeModbusEntity
from collections.abc import Callable as Callable, Coroutine, Mapping
from homeassistant.const import CONF_DEVICE as CONF_DEVICE, CONF_HOST as CONF_HOST, CONF_PORT as CONF_PORT, CONF_TYPE as CONF_TYPE
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from modbus_connection import ModbusSerialParams, ModbusTcpParams
from typing import Any, Concatenate

def create_modbus_params(data: Mapping[str, Any]) -> ModbusSerialParams | ModbusTcpParams: ...
def solaredge_exception_handler[_EntityT: SolarEdgeModbusEntity, **_P](func: Callable[Concatenate[_EntityT, _P], Coroutine[Any, Any, Any]]) -> Callable[Concatenate[_EntityT, _P], Coroutine[Any, Any, None]]: ...

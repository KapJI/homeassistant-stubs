from .const import CONF_KEYS as CONF_KEYS, CONF_LED as CONF_LED, CONF_OUTPUT as CONF_OUTPUT, CONF_PCK as CONF_PCK, CONF_RELVARREF as CONF_RELVARREF, CONF_ROW as CONF_ROW, CONF_SETPOINT as CONF_SETPOINT, CONF_TABLE as CONF_TABLE, CONF_TEXT as CONF_TEXT, CONF_TIME as CONF_TIME, CONF_TIME_UNIT as CONF_TIME_UNIT, CONF_TRANSITION as CONF_TRANSITION, CONF_VALUE as CONF_VALUE, CONF_VARIABLE as CONF_VARIABLE, DOMAIN as DOMAIN, LED_PORTS as LED_PORTS, LED_STATUS as LED_STATUS, OUTPUT_PORTS as OUTPUT_PORTS, RELVARREF as RELVARREF, SENDKEYCOMMANDS as SENDKEYCOMMANDS, SETPOINTS as SETPOINTS, THRESHOLDS as THRESHOLDS, TIME_UNITS as TIME_UNITS, VARIABLES as VARIABLES, VAR_UNITS as VAR_UNITS
from .helpers import DeviceConnectionType as DeviceConnectionType, get_device_connection as get_device_connection, is_address as is_address, is_states_string as is_states_string
from _typeshed import Incomplete
from homeassistant.const import CONF_ADDRESS as CONF_ADDRESS, CONF_BRIGHTNESS as CONF_BRIGHTNESS, CONF_HOST as CONF_HOST, CONF_STATE as CONF_STATE, CONF_UNIT_OF_MEASUREMENT as CONF_UNIT_OF_MEASUREMENT
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall

class LcnServiceCall:
    schema: Incomplete
    hass: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    def get_device_connection(self, service: ServiceCall) -> DeviceConnectionType: ...
    async def async_call_service(self, service: ServiceCall) -> None: ...

class OutputAbs(LcnServiceCall):
    schema: Incomplete
    async def async_call_service(self, service: ServiceCall) -> None: ...

class OutputRel(LcnServiceCall):
    schema: Incomplete
    async def async_call_service(self, service: ServiceCall) -> None: ...

class OutputToggle(LcnServiceCall):
    schema: Incomplete
    async def async_call_service(self, service: ServiceCall) -> None: ...

class Relays(LcnServiceCall):
    schema: Incomplete
    async def async_call_service(self, service: ServiceCall) -> None: ...

class Led(LcnServiceCall):
    schema: Incomplete
    async def async_call_service(self, service: ServiceCall) -> None: ...

class VarAbs(LcnServiceCall):
    schema: Incomplete
    async def async_call_service(self, service: ServiceCall) -> None: ...

class VarReset(LcnServiceCall):
    schema: Incomplete
    async def async_call_service(self, service: ServiceCall) -> None: ...

class VarRel(LcnServiceCall):
    schema: Incomplete
    async def async_call_service(self, service: ServiceCall) -> None: ...

class LockRegulator(LcnServiceCall):
    schema: Incomplete
    async def async_call_service(self, service: ServiceCall) -> None: ...

class SendKeys(LcnServiceCall):
    schema: Incomplete
    async def async_call_service(self, service: ServiceCall) -> None: ...

class LockKeys(LcnServiceCall):
    schema: Incomplete
    async def async_call_service(self, service: ServiceCall) -> None: ...

class DynText(LcnServiceCall):
    schema: Incomplete
    async def async_call_service(self, service: ServiceCall) -> None: ...

class Pck(LcnServiceCall):
    schema: Incomplete
    async def async_call_service(self, service: ServiceCall) -> None: ...

SERVICES: Incomplete

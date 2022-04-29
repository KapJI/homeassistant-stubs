import pysnmp.hlapi.asyncio as hlapi
from .const import DOMAIN as DOMAIN, SNMP as SNMP
from _typeshed import Incomplete
from homeassistant.const import EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import singleton as singleton

_LOGGER: Incomplete

def get_snmp_engine(hass: HomeAssistant) -> hlapi.SnmpEngine: ...

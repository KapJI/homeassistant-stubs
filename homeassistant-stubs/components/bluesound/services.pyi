import voluptuous as vol
from .const import ATTR_MASTER as ATTR_MASTER, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall
from typing import NamedTuple

SERVICE_CLEAR_TIMER: str
SERVICE_JOIN: str
SERVICE_SET_TIMER: str
SERVICE_UNJOIN: str
BS_SCHEMA: Incomplete
BS_JOIN_SCHEMA: Incomplete

class ServiceMethodDetails(NamedTuple):
    method: str
    schema: vol.Schema

SERVICE_TO_METHOD: Incomplete

def setup_services(hass: HomeAssistant) -> None: ...

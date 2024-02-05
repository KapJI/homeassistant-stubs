from . import KNXModule as KNXModule
from .const import DOMAIN as DOMAIN, KNX_ADDRESS as KNX_ADDRESS, SERVICE_KNX_ATTR_PAYLOAD as SERVICE_KNX_ATTR_PAYLOAD, SERVICE_KNX_ATTR_REMOVE as SERVICE_KNX_ATTR_REMOVE, SERVICE_KNX_ATTR_RESPONSE as SERVICE_KNX_ATTR_RESPONSE, SERVICE_KNX_ATTR_TYPE as SERVICE_KNX_ATTR_TYPE, SERVICE_KNX_EVENT_REGISTER as SERVICE_KNX_EVENT_REGISTER, SERVICE_KNX_EXPOSURE_REGISTER as SERVICE_KNX_EXPOSURE_REGISTER, SERVICE_KNX_READ as SERVICE_KNX_READ, SERVICE_KNX_SEND as SERVICE_KNX_SEND
from .expose import create_knx_exposure as create_knx_exposure
from .schema import ExposeSchema as ExposeSchema, ga_validator as ga_validator, sensor_type_validator as sensor_type_validator
from _typeshed import Incomplete
from homeassistant.const import CONF_TYPE as CONF_TYPE, SERVICE_RELOAD as SERVICE_RELOAD
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, ServiceValidationError as ServiceValidationError
from homeassistant.helpers.service import async_register_admin_service as async_register_admin_service

_LOGGER: Incomplete

def register_knx_services(hass: HomeAssistant) -> None: ...
def get_knx_module(hass: HomeAssistant) -> KNXModule: ...

SERVICE_KNX_EVENT_REGISTER_SCHEMA: Incomplete

async def service_event_register_modify(hass: HomeAssistant, call: ServiceCall) -> None: ...

SERVICE_KNX_EXPOSURE_REGISTER_SCHEMA: Incomplete

async def service_exposure_register_modify(hass: HomeAssistant, call: ServiceCall) -> None: ...

SERVICE_KNX_SEND_SCHEMA: Incomplete

async def service_send_to_knx_bus(hass: HomeAssistant, call: ServiceCall) -> None: ...

SERVICE_KNX_READ_SCHEMA: Incomplete

async def service_read_to_knx_bus(hass: HomeAssistant, call: ServiceCall) -> None: ...
async def service_reload_integration(hass: HomeAssistant, call: ServiceCall) -> None: ...

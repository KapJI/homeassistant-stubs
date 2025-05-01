from . import RenaultConfigEntry as RenaultConfigEntry
from .const import DOMAIN as DOMAIN
from .renault_vehicle import RenaultVehicleProxy as RenaultVehicleProxy
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall
from homeassistant.exceptions import ServiceValidationError as ServiceValidationError

LOGGER: Incomplete
ATTR_SCHEDULES: str
ATTR_TEMPERATURE: str
ATTR_VEHICLE: str
ATTR_WHEN: str
SERVICE_VEHICLE_SCHEMA: Incomplete
SERVICE_AC_START_SCHEMA: Incomplete
SERVICE_CHARGE_SET_SCHEDULE_DAY_SCHEMA: Incomplete
SERVICE_CHARGE_SET_SCHEDULE_SCHEMA: Incomplete
SERVICE_CHARGE_SET_SCHEDULES_SCHEMA: Incomplete
SERVICE_AC_SET_SCHEDULE_DAY_SCHEMA: Incomplete
SERVICE_AC_SET_SCHEDULE_SCHEMA: Incomplete
SERVICE_AC_SET_SCHEDULES_SCHEMA: Incomplete
SERVICE_AC_CANCEL: str
SERVICE_AC_START: str
SERVICE_CHARGE_SET_SCHEDULES: str
SERVICE_AC_SET_SCHEDULES: str
SERVICES: Incomplete

async def ac_cancel(service_call: ServiceCall) -> None: ...
async def ac_start(service_call: ServiceCall) -> None: ...
async def charge_set_schedules(service_call: ServiceCall) -> None: ...
async def ac_set_schedules(service_call: ServiceCall) -> None: ...
def get_vehicle_proxy(service_call: ServiceCall) -> RenaultVehicleProxy: ...
def setup_services(hass: HomeAssistant) -> None: ...

from .const import DOMAIN as DOMAIN
from .renault_hub import RenaultHub as RenaultHub
from .renault_vehicle import RenaultVehicleProxy as RenaultVehicleProxy
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall

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
SERVICE_AC_CANCEL: str
SERVICE_AC_START: str
SERVICE_CHARGE_SET_SCHEDULES: str
SERVICE_CHARGE_START: str
SERVICES: Incomplete

def setup_services(hass: HomeAssistant) -> None: ...
def unload_services(hass: HomeAssistant) -> None: ...

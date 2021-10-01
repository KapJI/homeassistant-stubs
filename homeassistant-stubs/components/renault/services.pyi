from .const import DOMAIN as DOMAIN
from .renault_hub import RenaultHub as RenaultHub
from .renault_vehicle import RenaultVehicleProxy as RenaultVehicleProxy
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall
from typing import Any

LOGGER: Any
ATTR_SCHEDULES: str
ATTR_TEMPERATURE: str
ATTR_VEHICLE: str
ATTR_WHEN: str
SERVICE_VEHICLE_SCHEMA: Any
SERVICE_AC_START_SCHEMA: Any
SERVICE_CHARGE_SET_SCHEDULE_DAY_SCHEMA: Any
SERVICE_CHARGE_SET_SCHEDULE_SCHEMA: Any
SERVICE_CHARGE_SET_SCHEDULES_SCHEMA: Any
SERVICE_AC_CANCEL: str
SERVICE_AC_START: str
SERVICE_CHARGE_SET_SCHEDULES: str
SERVICE_CHARGE_START: str
SERVICES: Any

def setup_services(hass: HomeAssistant) -> None: ...
def unload_services(hass: HomeAssistant) -> None: ...

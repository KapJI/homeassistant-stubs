from .const import DOMAIN as DOMAIN
from .helpers import handle_command as handle_command, handle_vehicle_command as handle_vehicle_command
from .models import TeslemetryEnergyData as TeslemetryEnergyData, TeslemetryVehicleData as TeslemetryVehicleData
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_LATITUDE as CONF_LATITUDE, CONF_LONGITUDE as CONF_LONGITUDE
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, ServiceValidationError as ServiceValidationError
from homeassistant.helpers import device_registry as dr

_LOGGER: Incomplete
ATTR_ID: str
ATTR_GPS: str
ATTR_TYPE: str
ATTR_VALUE: str
ATTR_LOCATION: str
ATTR_LOCALE: str
ATTR_ORDER: str
ATTR_TIMESTAMP: str
ATTR_FIELDS: str
ATTR_ENABLE: str
ATTR_TIME: str
ATTR_PIN: str
ATTR_TOU_SETTINGS: str
ATTR_PRECONDITIONING_ENABLED: str
ATTR_PRECONDITIONING_WEEKDAYS: str
ATTR_DEPARTURE_TIME: str
ATTR_OFF_PEAK_CHARGING_ENABLED: str
ATTR_OFF_PEAK_CHARGING_WEEKDAYS: str
ATTR_END_OFF_PEAK_TIME: str
ATTR_DAYS_OF_WEEK: str
ATTR_START_TIME: str
ATTR_END_TIME: str
ATTR_ONE_TIME: str
ATTR_NAME: str
ATTR_PRECONDITION_TIME: str
SERVICE_NAVIGATE_ATTR_GPS_REQUEST: str
SERVICE_SET_SCHEDULED_CHARGING: str
SERVICE_SET_SCHEDULED_DEPARTURE: str
SERVICE_VALET_MODE: str
SERVICE_SPEED_LIMIT: str
SERVICE_TIME_OF_USE: str
SERVICE_ADD_CHARGE_SCHEDULE: str
SERVICE_REMOVE_CHARGE_SCHEDULE: str
SERVICE_ADD_PRECONDITION_SCHEDULE: str
SERVICE_REMOVE_PRECONDITION_SCHEDULE: str

def async_get_device_for_service_call(hass: HomeAssistant, call: ServiceCall) -> dr.DeviceEntry: ...
def async_get_config_for_device(hass: HomeAssistant, device_entry: dr.DeviceEntry) -> ConfigEntry: ...
def async_get_vehicle_for_entry(hass: HomeAssistant, device: dr.DeviceEntry, config: ConfigEntry) -> TeslemetryVehicleData: ...
def async_get_energy_site_for_entry(hass: HomeAssistant, device: dr.DeviceEntry, config: ConfigEntry) -> TeslemetryEnergyData: ...
@callback
def async_setup_services(hass: HomeAssistant) -> None: ...

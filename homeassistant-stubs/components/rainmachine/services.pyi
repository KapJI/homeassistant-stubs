from . import RainMachineConfigEntry as RainMachineConfigEntry
from .const import CONF_DURATION as CONF_DURATION, DATA_PROGRAMS as DATA_PROGRAMS, DATA_ZONES as DATA_ZONES, DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.config_entries import ConfigEntryState as ConfigEntryState
from homeassistant.const import CONF_CONDITION as CONF_CONDITION, CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_UNIT_OF_MEASUREMENT as CONF_UNIT_OF_MEASUREMENT
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.util.dt import as_timestamp as as_timestamp, utcnow as utcnow
from regenmaschine.controller import Controller as Controller

API_URL_REFERENCE: str
CONF_DEWPOINT: str
CONF_ET: str
CONF_MAXRH: str
CONF_MAXTEMP: str
CONF_MINRH: str
CONF_MINTEMP: str
CONF_PRESSURE: str
CONF_QPF: str
CONF_RAIN: str
CONF_SECONDS: str
CONF_SOLARRAD: str
CONF_TEMPERATURE: str
CONF_TIMESTAMP: str
CONF_VALUE: str
CONF_WEATHER: str
CONF_WIND: str
CV_FLOW_METER_VALID_UNITS: Incomplete
CV_WX_DATA_VALID_PERCENTAGE: Incomplete
CV_WX_DATA_VALID_TEMP_RANGE: Incomplete
CV_WX_DATA_VALID_RAIN_RANGE: Incomplete
CV_WX_DATA_VALID_WIND_SPEED: Incomplete
CV_WX_DATA_VALID_PRESSURE: Incomplete
CV_WX_DATA_VALID_SOLARRAD: Incomplete
SERVICE_NAME_PAUSE_WATERING: str
SERVICE_NAME_PUSH_FLOW_METER_DATA: str
SERVICE_NAME_PUSH_WEATHER_DATA: str
SERVICE_NAME_RESTRICT_WATERING: str
SERVICE_NAME_STOP_ALL: str
SERVICE_NAME_UNPAUSE_WATERING: str
SERVICE_NAME_UNRESTRICT_WATERING: str
SERVICE_SCHEMA: Incomplete
SERVICE_PAUSE_WATERING_SCHEMA: Incomplete
SERVICE_PUSH_FLOW_METER_DATA_SCHEMA: Incomplete
SERVICE_PUSH_WEATHER_DATA_SCHEMA: Incomplete
SERVICE_RESTRICT_WATERING_SCHEMA: Incomplete

async def async_update_programs_and_zones(hass: HomeAssistant, entry: RainMachineConfigEntry) -> None: ...
@callback
def async_get_entry_for_service_call(hass: HomeAssistant, call: ServiceCall) -> RainMachineConfigEntry: ...
@callback
def async_setup_services(hass: HomeAssistant) -> None: ...

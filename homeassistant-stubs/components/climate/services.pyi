from . import ClimateEntity as ClimateEntity
from .const import ATTR_FAN_MODE as ATTR_FAN_MODE, ATTR_HUMIDITY as ATTR_HUMIDITY, ATTR_HVAC_MODE as ATTR_HVAC_MODE, ATTR_PRESET_MODE as ATTR_PRESET_MODE, ATTR_SWING_HORIZONTAL_MODE as ATTR_SWING_HORIZONTAL_MODE, ATTR_SWING_MODE as ATTR_SWING_MODE, ATTR_TARGET_TEMP_HIGH as ATTR_TARGET_TEMP_HIGH, ATTR_TARGET_TEMP_LOW as ATTR_TARGET_TEMP_LOW, ClimateEntityFeature as ClimateEntityFeature, DATA_COMPONENT as DATA_COMPONENT, DOMAIN as DOMAIN, HVACMode as HVACMode, SERVICE_SET_FAN_MODE as SERVICE_SET_FAN_MODE, SERVICE_SET_HUMIDITY as SERVICE_SET_HUMIDITY, SERVICE_SET_HVAC_MODE as SERVICE_SET_HVAC_MODE, SERVICE_SET_PRESET_MODE as SERVICE_SET_PRESET_MODE, SERVICE_SET_SWING_HORIZONTAL_MODE as SERVICE_SET_SWING_HORIZONTAL_MODE, SERVICE_SET_SWING_MODE as SERVICE_SET_SWING_MODE, SERVICE_SET_TEMPERATURE as SERVICE_SET_TEMPERATURE
from _typeshed import Incomplete
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, SERVICE_TOGGLE as SERVICE_TOGGLE, SERVICE_TURN_OFF as SERVICE_TURN_OFF, SERVICE_TURN_ON as SERVICE_TURN_ON
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.exceptions import ServiceValidationError as ServiceValidationError
from homeassistant.util.unit_conversion import TemperatureConverter as TemperatureConverter

_LOGGER: Incomplete
CONVERTIBLE_ATTRIBUTE: Incomplete
SET_TEMPERATURE_SCHEMA: Incomplete

async def _async_service_humidity_set(entity: ClimateEntity, service_call: ServiceCall) -> None: ...
async def _async_service_temperature_set(entity: ClimateEntity, service_call: ServiceCall) -> None: ...
@callback
def async_setup_services(hass: HomeAssistant) -> None: ...

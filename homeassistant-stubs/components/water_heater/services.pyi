from . import WaterHeaterEntity as WaterHeaterEntity
from .const import ATTR_AWAY_MODE as ATTR_AWAY_MODE, ATTR_OPERATION_MODE as ATTR_OPERATION_MODE, DATA_COMPONENT as DATA_COMPONENT, SERVICE_SET_AWAY_MODE as SERVICE_SET_AWAY_MODE, SERVICE_SET_OPERATION_MODE as SERVICE_SET_OPERATION_MODE, SERVICE_SET_TEMPERATURE as SERVICE_SET_TEMPERATURE, WaterHeaterEntityFeature as WaterHeaterEntityFeature
from _typeshed import Incomplete
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, SERVICE_TURN_OFF as SERVICE_TURN_OFF, SERVICE_TURN_ON as SERVICE_TURN_ON
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.helpers.typing import VolDictType as VolDictType
from homeassistant.util.unit_conversion import TemperatureConverter as TemperatureConverter

CONVERTIBLE_ATTRIBUTE: Incomplete
SET_AWAY_MODE_SCHEMA: VolDictType
SET_TEMPERATURE_SCHEMA: VolDictType
SET_OPERATION_MODE_SCHEMA: VolDictType

async def _async_service_away_mode(entity: WaterHeaterEntity, service: ServiceCall) -> None: ...
async def _async_service_temperature_set(entity: WaterHeaterEntity, service: ServiceCall) -> None: ...
@callback
def async_setup_services(hass: HomeAssistant) -> None: ...

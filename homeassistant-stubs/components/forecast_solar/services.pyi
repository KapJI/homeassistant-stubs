from .const import DOMAIN as DOMAIN
from .coordinator import ForecastSolarConfigEntry as ForecastSolarConfigEntry
from _typeshed import Incomplete
from datetime import datetime
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, ServiceResponse as ServiceResponse, SupportsResponse as SupportsResponse, callback as callback
from homeassistant.exceptions import ServiceValidationError as ServiceValidationError
from homeassistant.helpers import service as service
from homeassistant.helpers.selector import ConfigEntrySelector as ConfigEntrySelector
from homeassistant.util.json import JsonValueType as JsonValueType

ATTR_CONFIG_ENTRY: str
ATTR_START: str
ATTR_END: str
ATTR_RESOLUTION: str
RESOLUTION_RAW: str
RESOLUTION_HOURLY: str
SERVICE_GET_FORECAST: str
GET_FORECAST_SCHEMA: Incomplete

def _aggregate_hourly(watts: dict[datetime, int], wh_period: dict[datetime, int]) -> tuple[dict[datetime, float], dict[datetime, int]]: ...
@callback
def async_setup_services(hass: HomeAssistant) -> None: ...

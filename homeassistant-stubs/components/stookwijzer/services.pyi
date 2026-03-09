from .const import DOMAIN as DOMAIN, SERVICE_GET_FORECAST as SERVICE_GET_FORECAST
from .coordinator import StookwijzerConfigEntry as StookwijzerConfigEntry
from _typeshed import Incomplete
from homeassistant.const import ATTR_CONFIG_ENTRY_ID as ATTR_CONFIG_ENTRY_ID
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, ServiceResponse as ServiceResponse, SupportsResponse as SupportsResponse, callback as callback
from homeassistant.helpers import service as service
from typing import Required, TypedDict

SERVICE_GET_FORECAST_SCHEMA: Incomplete

class Forecast(TypedDict):
    datetime: Required[str]
    advice: str | None
    final: bool | None

@callback
def async_setup_services(hass: HomeAssistant) -> None: ...

from .const import ATTR_CONFIG_ENTRY_ID as ATTR_CONFIG_ENTRY_ID, DOMAIN as DOMAIN, SERVICE_GET_FORECAST as SERVICE_GET_FORECAST
from .coordinator import StookwijzerConfigEntry as StookwijzerConfigEntry
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntryState as ConfigEntryState
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, ServiceResponse as ServiceResponse, SupportsResponse as SupportsResponse
from homeassistant.exceptions import ServiceValidationError as ServiceValidationError
from typing import Required, TypedDict

SERVICE_GET_FORECAST_SCHEMA: Incomplete

class Forecast(TypedDict):
    datetime: Required[str]
    advice: str | None
    final: bool | None

def async_get_entry(hass: HomeAssistant, config_entry_id: str) -> StookwijzerConfigEntry: ...
def setup_services(hass: HomeAssistant) -> None: ...

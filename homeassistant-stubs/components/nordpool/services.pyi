from . import NordPoolConfigEntry as NordPoolConfigEntry
from .const import ATTR_RESOLUTION as ATTR_RESOLUTION, DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.config_entries import ConfigEntryState as ConfigEntryState
from homeassistant.const import ATTR_DATE as ATTR_DATE
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, ServiceResponse as ServiceResponse, SupportsResponse as SupportsResponse, callback as callback
from homeassistant.exceptions import ServiceValidationError as ServiceValidationError
from homeassistant.helpers.selector import ConfigEntrySelector as ConfigEntrySelector
from homeassistant.util.json import JsonValueType as JsonValueType
from pynordpool import DeliveryPeriodData as DeliveryPeriodData, NordPoolClient as NordPoolClient, PriceIndicesData as PriceIndicesData

_LOGGER: Incomplete
ATTR_CONFIG_ENTRY: str
ATTR_AREAS: str
ATTR_CURRENCY: str
SERVICE_GET_PRICES_FOR_DATE: str
SERVICE_GET_PRICE_INDICES_FOR_DATE: str
SERVICE_GET_PRICES_SCHEMA: Incomplete
SERVICE_GET_PRICE_INDICES_SCHEMA: Incomplete

def get_config_entry(hass: HomeAssistant, entry_id: str) -> NordPoolConfigEntry: ...
@callback
def async_setup_services(hass: HomeAssistant) -> None: ...

from .const import DOMAIN as DOMAIN
from .coordinator import EnergyZeroDataUpdateCoordinator as EnergyZeroDataUpdateCoordinator
from _typeshed import Incomplete
from datetime import date, datetime
from energyzero import Electricity as Electricity, Gas as Gas
from enum import Enum
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigEntryState as ConfigEntryState
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, ServiceResponse as ServiceResponse, SupportsResponse as SupportsResponse, callback as callback
from homeassistant.exceptions import ServiceValidationError as ServiceValidationError
from homeassistant.helpers import selector as selector
from typing import Final

ATTR_CONFIG_ENTRY: Final[str]
ATTR_START: Final[str]
ATTR_END: Final[str]
ATTR_INCL_VAT: Final[str]
GAS_SERVICE_NAME: Final[str]
ENERGY_SERVICE_NAME: Final[str]
SERVICE_SCHEMA: Final[Incomplete]

class PriceType(Enum):
    ENERGY: str
    GAS: str

def __get_date(date_input: str | None) -> date | datetime: ...
def __serialize_prices(prices: Electricity | Gas) -> ServiceResponse: ...
def __get_coordinator(hass: HomeAssistant, call: ServiceCall) -> EnergyZeroDataUpdateCoordinator: ...
async def __get_prices(call: ServiceCall, *, hass: HomeAssistant, price_type: PriceType) -> ServiceResponse: ...
def async_setup_services(hass: HomeAssistant) -> None: ...

from .const import DOMAIN as DOMAIN
from .coordinator import EnergyZeroConfigEntry as EnergyZeroConfigEntry, EnergyZeroDataUpdateCoordinator as EnergyZeroDataUpdateCoordinator
from _typeshed import Incomplete
from datetime import date, datetime
from energyzero import EnergyPrices as EnergyPrices
from enum import Enum
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, ServiceResponse as ServiceResponse, SupportsResponse as SupportsResponse, callback as callback
from homeassistant.exceptions import ServiceValidationError as ServiceValidationError
from homeassistant.helpers import selector as selector, service as service
from typing import Final
from zoneinfo import ZoneInfo

ATTR_CONFIG_ENTRY: Final[str]
ATTR_START: Final[str]
ATTR_END: Final[str]
ATTR_INCL_VAT: Final[str]
GAS_SERVICE_NAME: Final[str]
ENERGY_SERVICE_NAME: Final[str]
SERVICE_SCHEMA: Final[Incomplete]

class ServicePriceType(Enum):
    ENERGY = 'energy'
    GAS = 'gas'

def __get_date(date_input: str | None, local_tz: ZoneInfo) -> tuple[date, datetime | None]: ...
def __serialize_prices(prices: list[EnergyPrices], start: datetime, end: datetime) -> ServiceResponse: ...
def __get_coordinator(call: ServiceCall) -> EnergyZeroDataUpdateCoordinator: ...
async def __get_prices(call: ServiceCall, *, price_type: ServicePriceType) -> ServiceResponse: ...
@callback
def async_setup_services(hass: HomeAssistant) -> None: ...

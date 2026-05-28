from .const import DOMAIN as DOMAIN
from .coordinator import EasyEnergyConfigEntry as EasyEnergyConfigEntry, EasyEnergyDataUpdateCoordinator as EasyEnergyDataUpdateCoordinator
from _typeshed import Incomplete
from datetime import date, datetime
from easyenergy import Electricity as Electricity, Gas as Gas, PriceInterval as PriceInterval
from enum import StrEnum
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, ServiceResponse as ServiceResponse, SupportsResponse as SupportsResponse, callback as callback
from homeassistant.exceptions import ServiceValidationError as ServiceValidationError
from homeassistant.helpers import selector as selector, service as service
from typing import Final

ATTR_CONFIG_ENTRY: Final[str]
ATTR_START: Final[str]
ATTR_END: Final[str]
ATTR_INCL_VAT: Final[str]
ATTR_GRANULARITY: Final[str]
ATTR_PRICE_TYPE: Final[str]
GAS_SERVICE_NAME: Final[str]
ENERGY_USAGE_SERVICE_NAME: Final[str]
ENERGY_RETURN_SERVICE_NAME: Final[str]

class ServicePriceType(StrEnum):
    ENERGY_USAGE = 'energy_usage'
    ENERGY_RETURN = 'energy_return'
    GAS = 'gas'

GRANULARITY_OPTIONS: Final[Incomplete]
PRICE_TYPE_OPTIONS: Final[Incomplete]
BASE_SERVICE_SCHEMA: Final[Incomplete]
GAS_SERVICE_SCHEMA: Final[Incomplete]
ENERGY_USAGE_SERVICE_SCHEMA: Final[Incomplete]
ENERGY_RETURN_SERVICE_SCHEMA: Final[Incomplete]

def __get_date(date_input: str | None) -> tuple[date, datetime | None]: ...
def __filter_prices(prices: list[dict[str, float | datetime]], intervals: tuple[PriceInterval, ...], start: datetime, end: datetime) -> list[dict[str, float | datetime]]: ...
def __serialize_prices(prices: list[dict[str, float | datetime]]) -> ServiceResponse: ...
def __select_prices(data: Electricity | Gas, use_invoice: bool) -> list[dict[str, float | datetime]]: ...
def __get_coordinator(call: ServiceCall) -> EasyEnergyDataUpdateCoordinator: ...
async def __get_prices(call: ServiceCall, *, service_price_type: ServicePriceType) -> ServiceResponse: ...
@callback
def async_setup_services(hass: HomeAssistant) -> None: ...

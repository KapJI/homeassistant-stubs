from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from datetime import date, datetime
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, ServiceResponse as ServiceResponse, SupportsResponse as SupportsResponse, callback as callback
from homeassistant.exceptions import ServiceValidationError as ServiceValidationError
from typing import Final

PRICE_SERVICE_NAME: str
ATTR_START: Final[str]
ATTR_END: Final[str]
SERVICE_SCHEMA: Final[Incomplete]

async def __get_prices(call: ServiceCall, *, hass: HomeAssistant) -> ServiceResponse: ...
def __get_date(date_input: str | None, mode: str | None) -> date | datetime: ...
def async_setup_services(hass: HomeAssistant) -> None: ...

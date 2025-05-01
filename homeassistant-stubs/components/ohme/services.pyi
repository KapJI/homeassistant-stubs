from .const import DOMAIN as DOMAIN
from .coordinator import OhmeConfigEntry as OhmeConfigEntry
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntryState as ConfigEntryState
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, ServiceResponse as ServiceResponse, SupportsResponse as SupportsResponse
from homeassistant.exceptions import ServiceValidationError as ServiceValidationError
from homeassistant.helpers import selector as selector
from ohme import OhmeApiClient as OhmeApiClient
from typing import Final

ATTR_CONFIG_ENTRY: Final[str]
ATTR_PRICE_CAP: Final[str]
SERVICE_LIST_CHARGE_SLOTS: str
SERVICE_LIST_CHARGE_SLOTS_SCHEMA: Final[Incomplete]
SERVICE_SET_PRICE_CAP: str
SERVICE_SET_PRICE_CAP_SCHEMA: Final[Incomplete]

def __get_client(call: ServiceCall) -> OhmeApiClient: ...
def async_setup_services(hass: HomeAssistant) -> None: ...

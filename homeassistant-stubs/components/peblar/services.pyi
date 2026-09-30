from .const import CONF_EVCC_ID as CONF_EVCC_ID, CONF_UID as CONF_UID, DOMAIN as DOMAIN
from .coordinator import PeblarConfigEntry as PeblarConfigEntry
from _typeshed import Incomplete
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from homeassistant.const import ATTR_CONFIG_ENTRY_ID as ATTR_CONFIG_ENTRY_ID, CONF_ALIAS as CONF_ALIAS, CONF_DESCRIPTION as CONF_DESCRIPTION
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, ServiceResponse as ServiceResponse, SupportsResponse as SupportsResponse, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, ServiceValidationError as ServiceValidationError
from homeassistant.helpers.service import async_get_config_entry as async_get_config_entry, async_register_admin_service as async_register_admin_service
from peblar import Peblar as Peblar, PeblarApi as PeblarApi

SERVICE_ADD_RFID_TOKEN: str
SERVICE_AUTHORIZE_CHARGE_SESSION: str
SERVICE_ADD_VEHICLE_TOKEN: str
SERVICE_DELETE_RFID_TOKEN: str
SERVICE_DELETE_VEHICLE_TOKEN: str
SERVICE_LIST_RFID_TOKENS: str
SERVICE_LIST_VEHICLE_TOKENS: str
CHARGER_SCHEMA: Incomplete
TOKEN_SCHEMA: Incomplete
ADD_TOKEN_SCHEMA: Incomplete
VEHICLE_SCHEMA: Incomplete
ADD_VEHICLE_SCHEMA: Incomplete
AUTHORIZE_SCHEMA: Incomplete

def _get_rfid_peblar(hass: HomeAssistant, entry_id: str) -> Peblar: ...
def _get_authorizing_api(hass: HomeAssistant, entry_id: str) -> PeblarApi: ...
def _get_autocharge_peblar(hass: HomeAssistant, entry_id: str) -> Peblar: ...
@asynccontextmanager
async def _handle_peblar_errors(hass: HomeAssistant, entry_id: str) -> AsyncIterator[None]: ...
@callback
def async_setup_services(hass: HomeAssistant) -> None: ...

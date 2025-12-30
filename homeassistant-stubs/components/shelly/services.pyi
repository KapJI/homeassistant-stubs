from .const import ATTR_KEY as ATTR_KEY, ATTR_VALUE as ATTR_VALUE, CONF_SLEEP_PERIOD as CONF_SLEEP_PERIOD, DOMAIN as DOMAIN
from .coordinator import ShellyConfigEntry as ShellyConfigEntry
from .utils import get_device_entry_gen as get_device_entry_gen
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntryState as ConfigEntryState
from homeassistant.const import ATTR_DEVICE_ID as ATTR_DEVICE_ID
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, ServiceResponse as ServiceResponse, SupportsResponse as SupportsResponse, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, ServiceValidationError as ServiceValidationError
from homeassistant.util.json import JsonValueType as JsonValueType
from typing import Any

SERVICE_GET_KVS_VALUE: str
SERVICE_SET_KVS_VALUE: str
SERVICE_GET_KVS_VALUE_SCHEMA: Incomplete
SERVICE_SET_KVS_VALUE_SCHEMA: Incomplete

@callback
def async_get_config_entry_for_service_call(call: ServiceCall) -> ShellyConfigEntry: ...
async def _async_execute_action(call: ServiceCall, method: str, args: tuple) -> dict[str, Any]: ...
async def async_get_kvs_value(call: ServiceCall) -> ServiceResponse: ...
async def async_set_kvs_value(call: ServiceCall) -> None: ...
@callback
def async_setup_services(hass: HomeAssistant) -> None: ...

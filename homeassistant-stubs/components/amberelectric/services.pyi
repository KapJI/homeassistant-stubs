from .const import ATTR_CHANNEL_TYPE as ATTR_CHANNEL_TYPE, CONTROLLED_LOAD_CHANNEL as CONTROLLED_LOAD_CHANNEL, DOMAIN as DOMAIN, FEED_IN_CHANNEL as FEED_IN_CHANNEL, GENERAL_CHANNEL as GENERAL_CHANNEL, SERVICE_GET_FORECASTS as SERVICE_GET_FORECASTS
from .coordinator import AmberConfigEntry as AmberConfigEntry
from .helpers import format_cents_to_dollars as format_cents_to_dollars, normalize_descriptor as normalize_descriptor
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntryState as ConfigEntryState
from homeassistant.const import ATTR_CONFIG_ENTRY_ID as ATTR_CONFIG_ENTRY_ID
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, ServiceResponse as ServiceResponse, SupportsResponse as SupportsResponse, callback as callback
from homeassistant.exceptions import ServiceValidationError as ServiceValidationError
from homeassistant.helpers.selector import ConfigEntrySelector as ConfigEntrySelector
from homeassistant.util.json import JsonValueType as JsonValueType

GET_FORECASTS_SCHEMA: Incomplete

def async_get_entry(hass: HomeAssistant, config_entry_id: str) -> AmberConfigEntry: ...
def get_forecasts(channel_type: str, data: dict) -> list[JsonValueType]: ...
@callback
def async_setup_services(hass: HomeAssistant) -> None: ...

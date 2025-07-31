from .const import ATTR_ACTIVITY as ATTR_ACTIVITY, ATTR_REACTION as ATTR_REACTION, ATTR_RECEIVER as ATTR_RECEIVER, DOMAIN as DOMAIN, SERVICE_ACTIVITY_STREAM_REACTION as SERVICE_ACTIVITY_STREAM_REACTION
from .coordinator import BringConfigEntry as BringConfigEntry
from _typeshed import Incomplete
from homeassistant.components.event import ATTR_EVENT_TYPE as ATTR_EVENT_TYPE
from homeassistant.config_entries import ConfigEntryState as ConfigEntryState
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, ServiceValidationError as ServiceValidationError

_LOGGER: Incomplete
SERVICE_ACTIVITY_STREAM_REACTION_SCHEMA: Incomplete

def get_config_entry(hass: HomeAssistant, entry_id: str) -> BringConfigEntry: ...
def async_setup_services(hass: HomeAssistant) -> None: ...

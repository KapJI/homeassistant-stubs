from . import ATTR_SOURCE as ATTR_SOURCE, EVENT_AUTOMATION_TRIGGERED as EVENT_AUTOMATION_TRIGGERED
from .const import DOMAIN as DOMAIN
from homeassistant.components.logbook import LOGBOOK_ENTRY_CONTEXT_ID as LOGBOOK_ENTRY_CONTEXT_ID, LOGBOOK_ENTRY_ENTITY_ID as LOGBOOK_ENTRY_ENTITY_ID, LOGBOOK_ENTRY_MESSAGE as LOGBOOK_ENTRY_MESSAGE, LOGBOOK_ENTRY_NAME as LOGBOOK_ENTRY_NAME, LOGBOOK_ENTRY_SOURCE as LOGBOOK_ENTRY_SOURCE, LazyEventPartialState as LazyEventPartialState
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, ATTR_NAME as ATTR_NAME
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback

def async_describe_events(hass: HomeAssistant, async_describe_event): ...

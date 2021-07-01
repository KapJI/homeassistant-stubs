from . import ATTR_SOURCE as ATTR_SOURCE, DOMAIN as DOMAIN, EVENT_AUTOMATION_TRIGGERED as EVENT_AUTOMATION_TRIGGERED
from homeassistant.components.logbook import LazyEventPartialState as LazyEventPartialState
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, ATTR_NAME as ATTR_NAME
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback

def async_describe_events(hass: HomeAssistant, async_describe_event): ...

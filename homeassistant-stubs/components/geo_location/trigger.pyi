from homeassistant.components.geo_location import DOMAIN as DOMAIN
from homeassistant.const import CONF_EVENT as CONF_EVENT, CONF_PLATFORM as CONF_PLATFORM, CONF_SOURCE as CONF_SOURCE, CONF_ZONE as CONF_ZONE
from homeassistant.core import HassJob as HassJob, callback as callback
from homeassistant.helpers import condition as condition
from homeassistant.helpers.config_validation import entity_domain as entity_domain
from homeassistant.helpers.event import TrackStates as TrackStates, async_track_state_change_filtered as async_track_state_change_filtered
from typing import Any

_LOGGER: Any
EVENT_ENTER: str
EVENT_LEAVE: str
DEFAULT_EVENT = EVENT_ENTER
TRIGGER_SCHEMA: Any

def source_match(state, source): ...
async def async_attach_trigger(hass, config, action, automation_info): ...

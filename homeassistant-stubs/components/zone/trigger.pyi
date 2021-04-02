from homeassistant.const import ATTR_FRIENDLY_NAME as ATTR_FRIENDLY_NAME, CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_EVENT as CONF_EVENT, CONF_PLATFORM as CONF_PLATFORM, CONF_ZONE as CONF_ZONE
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HassJob as HassJob, callback as callback
from homeassistant.helpers import condition as condition, location as location
from homeassistant.helpers.event import async_track_state_change_event as async_track_state_change_event
from typing import Any

EVENT_ENTER: str
EVENT_LEAVE: str
DEFAULT_EVENT = EVENT_ENTER
_EVENT_DESCRIPTION: Any
TRIGGER_SCHEMA: Any

async def async_attach_trigger(hass: Any, config: Any, action: Any, automation_info: Any, *, platform_type: str=...) -> CALLBACK_TYPE: ...

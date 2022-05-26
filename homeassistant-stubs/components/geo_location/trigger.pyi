from . import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.automation import AutomationActionType as AutomationActionType, AutomationTriggerInfo as AutomationTriggerInfo
from homeassistant.const import CONF_EVENT as CONF_EVENT, CONF_PLATFORM as CONF_PLATFORM, CONF_SOURCE as CONF_SOURCE, CONF_ZONE as CONF_ZONE
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HassJob as HassJob, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import condition as condition
from homeassistant.helpers.config_validation import entity_domain as entity_domain
from homeassistant.helpers.event import TrackStates as TrackStates, async_track_state_change_filtered as async_track_state_change_filtered
from homeassistant.helpers.typing import ConfigType as ConfigType

_LOGGER: Incomplete
EVENT_ENTER: str
EVENT_LEAVE: str
DEFAULT_EVENT = EVENT_ENTER
TRIGGER_SCHEMA: Incomplete

def source_match(state, source): ...
async def async_attach_trigger(hass: HomeAssistant, config: ConfigType, action: AutomationActionType, automation_info: AutomationTriggerInfo) -> CALLBACK_TYPE: ...

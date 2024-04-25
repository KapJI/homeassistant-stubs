from _typeshed import Incomplete
from homeassistant.components import sensor as sensor
from homeassistant.const import ATTR_DEVICE_CLASS as ATTR_DEVICE_CLASS, CONF_AT as CONF_AT, CONF_PLATFORM as CONF_PLATFORM, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, Event as Event, EventStateChangedData as EventStateChangedData, HassJob as HassJob, HomeAssistant as HomeAssistant, State as State, callback as callback
from homeassistant.helpers.event import async_track_point_in_time as async_track_point_in_time, async_track_state_change_event as async_track_state_change_event, async_track_time_change as async_track_time_change
from homeassistant.helpers.trigger import TriggerActionType as TriggerActionType, TriggerInfo as TriggerInfo
from homeassistant.helpers.typing import ConfigType as ConfigType

_TIME_TRIGGER_SCHEMA: Incomplete
TRIGGER_SCHEMA: Incomplete

async def async_attach_trigger(hass: HomeAssistant, config: ConfigType, action: TriggerActionType, trigger_info: TriggerInfo) -> CALLBACK_TYPE: ...

from . import get_device_wrapper as get_device_wrapper
from .const import ATTR_CHANNEL as ATTR_CHANNEL, ATTR_CLICK_TYPE as ATTR_CLICK_TYPE, ATTR_DEVICE as ATTR_DEVICE, DOMAIN as DOMAIN, EVENT_SHELLY_CLICK as EVENT_SHELLY_CLICK
from .utils import get_device_name as get_device_name
from homeassistant.const import ATTR_DEVICE_ID as ATTR_DEVICE_ID
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.typing import EventType as EventType
from typing import Callable

def async_describe_events(hass: HomeAssistant, async_describe_event: Callable[[str, str, Callable[[EventType], dict]], None]) -> None: ...

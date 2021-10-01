from . import get_block_device_wrapper as get_block_device_wrapper, get_rpc_device_wrapper as get_rpc_device_wrapper
from .const import ATTR_CHANNEL as ATTR_CHANNEL, ATTR_CLICK_TYPE as ATTR_CLICK_TYPE, ATTR_DEVICE as ATTR_DEVICE, BLOCK_INPUTS_EVENTS_TYPES as BLOCK_INPUTS_EVENTS_TYPES, DOMAIN as DOMAIN, EVENT_SHELLY_CLICK as EVENT_SHELLY_CLICK, RPC_INPUTS_EVENTS_TYPES as RPC_INPUTS_EVENTS_TYPES
from .utils import get_block_device_name as get_block_device_name, get_rpc_entity_name as get_rpc_entity_name
from collections.abc import Callable as Callable
from homeassistant.const import ATTR_DEVICE_ID as ATTR_DEVICE_ID
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.typing import EventType as EventType

def async_describe_events(hass: HomeAssistant, async_describe_event: Callable[[str, str, Callable[[EventType], dict]], None]) -> None: ...

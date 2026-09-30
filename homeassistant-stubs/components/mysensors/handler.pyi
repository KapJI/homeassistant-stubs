from .const import CHILD_CALLBACK as CHILD_CALLBACK, DevId as DevId, NODE_CALLBACK as NODE_CALLBACK
from .helpers import discover_mysensors_node as discover_mysensors_node, discover_mysensors_platform as discover_mysensors_platform, validate_set_msg as validate_set_msg
from .models import MySensorsConfigEntry as MySensorsConfigEntry
from collections.abc import Callable as Callable
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send
from homeassistant.util import decorator as decorator
from mysensors import Message as Message

HANDLERS: decorator.Registry[str, Callable[[HomeAssistant, MySensorsConfigEntry, Message], None]]

@callback
def handle_set(hass: HomeAssistant, entry: MySensorsConfigEntry, msg: Message) -> None: ...
@callback
def handle_internal(hass: HomeAssistant, entry: MySensorsConfigEntry, msg: Message) -> None: ...
@callback
def handle_battery_level(hass: HomeAssistant, entry: MySensorsConfigEntry, msg: Message) -> None: ...
@callback
def handle_heartbeat(hass: HomeAssistant, entry: MySensorsConfigEntry, msg: Message) -> None: ...
@callback
def handle_sketch_name(hass: HomeAssistant, entry: MySensorsConfigEntry, msg: Message) -> None: ...
@callback
def handle_sketch_version(hass: HomeAssistant, entry: MySensorsConfigEntry, msg: Message) -> None: ...
@callback
def handle_presentation(hass: HomeAssistant, entry: MySensorsConfigEntry, msg: Message) -> None: ...
@callback
def _handle_child_update(hass: HomeAssistant, entry: MySensorsConfigEntry, validated: dict[Platform, list[DevId]]) -> None: ...
@callback
def _handle_node_update(hass: HomeAssistant, entry: MySensorsConfigEntry, msg: Message) -> None: ...

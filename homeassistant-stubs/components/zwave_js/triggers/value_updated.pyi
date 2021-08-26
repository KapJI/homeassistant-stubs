from homeassistant.components.zwave_js.const import ATTR_COMMAND_CLASS as ATTR_COMMAND_CLASS, ATTR_COMMAND_CLASS_NAME as ATTR_COMMAND_CLASS_NAME, ATTR_CURRENT_VALUE as ATTR_CURRENT_VALUE, ATTR_CURRENT_VALUE_RAW as ATTR_CURRENT_VALUE_RAW, ATTR_ENDPOINT as ATTR_ENDPOINT, ATTR_NODE_ID as ATTR_NODE_ID, ATTR_PREVIOUS_VALUE as ATTR_PREVIOUS_VALUE, ATTR_PREVIOUS_VALUE_RAW as ATTR_PREVIOUS_VALUE_RAW, ATTR_PROPERTY as ATTR_PROPERTY, ATTR_PROPERTY_KEY as ATTR_PROPERTY_KEY, ATTR_PROPERTY_KEY_NAME as ATTR_PROPERTY_KEY_NAME, ATTR_PROPERTY_NAME as ATTR_PROPERTY_NAME, DOMAIN as DOMAIN
from homeassistant.components.zwave_js.helpers import async_get_node_from_device_id as async_get_node_from_device_id, async_get_node_from_entity_id as async_get_node_from_entity_id, get_device_id as get_device_id
from homeassistant.const import ATTR_DEVICE_ID as ATTR_DEVICE_ID, ATTR_ENTITY_ID as ATTR_ENTITY_ID, CONF_PLATFORM as CONF_PLATFORM, MATCH_ALL as MATCH_ALL
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HassJob as HassJob, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any, Callable
from zwave_js_server.event import Event as Event
from zwave_js_server.model.node import Node as Node
from zwave_js_server.model.value import Value as Value

_LOGGER: Any
PLATFORM_TYPE: Any
ATTR_FROM: str
ATTR_TO: str
VALUE_SCHEMA: Any
TRIGGER_SCHEMA: Any

async def async_attach_trigger(hass: HomeAssistant, config: ConfigType, action: Callable, automation_info: dict[str, Any], *, platform_type: str = ...) -> CALLBACK_TYPE: ...

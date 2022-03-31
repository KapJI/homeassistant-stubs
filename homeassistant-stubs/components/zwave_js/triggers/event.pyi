from homeassistant.components.automation import AutomationActionType as AutomationActionType, AutomationTriggerInfo as AutomationTriggerInfo
from homeassistant.components.zwave_js.const import ATTR_CONFIG_ENTRY_ID as ATTR_CONFIG_ENTRY_ID, ATTR_EVENT as ATTR_EVENT, ATTR_EVENT_DATA as ATTR_EVENT_DATA, ATTR_EVENT_SOURCE as ATTR_EVENT_SOURCE, ATTR_NODES as ATTR_NODES, ATTR_NODE_ID as ATTR_NODE_ID, ATTR_PARTIAL_DICT_MATCH as ATTR_PARTIAL_DICT_MATCH, DATA_CLIENT as DATA_CLIENT, DOMAIN as DOMAIN
from homeassistant.components.zwave_js.helpers import async_get_nodes_from_targets as async_get_nodes_from_targets, get_device_id as get_device_id, get_home_and_node_id_from_device_entry as get_home_and_node_id_from_device_entry
from homeassistant.config_entries import ConfigEntryState as ConfigEntryState
from homeassistant.const import ATTR_DEVICE_ID as ATTR_DEVICE_ID, ATTR_ENTITY_ID as ATTR_ENTITY_ID, CONF_PLATFORM as CONF_PLATFORM
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HassJob as HassJob, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any
from zwave_js_server.client import Client as Client
from zwave_js_server.model.node import Node as Node

PLATFORM_TYPE: Any
EVENT_MODEL_MAP: Any

def validate_non_node_event_source(obj: dict) -> dict: ...
def validate_event_name(obj: dict) -> dict: ...
def validate_event_data(obj: dict) -> dict: ...

TRIGGER_SCHEMA: Any

async def async_validate_trigger_config(hass: HomeAssistant, config: ConfigType) -> ConfigType: ...
async def async_attach_trigger(hass: HomeAssistant, config: ConfigType, action: AutomationActionType, automation_info: AutomationTriggerInfo, *, platform_type: str = ...) -> CALLBACK_TYPE: ...

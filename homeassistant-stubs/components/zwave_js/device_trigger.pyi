import voluptuous as vol
from . import trigger as trigger
from .const import ATTR_COMMAND_CLASS as ATTR_COMMAND_CLASS, ATTR_DATA_TYPE as ATTR_DATA_TYPE, ATTR_ENDPOINT as ATTR_ENDPOINT, ATTR_EVENT as ATTR_EVENT, ATTR_EVENT_LABEL as ATTR_EVENT_LABEL, ATTR_EVENT_TYPE as ATTR_EVENT_TYPE, ATTR_LABEL as ATTR_LABEL, ATTR_PROPERTY as ATTR_PROPERTY, ATTR_PROPERTY_KEY as ATTR_PROPERTY_KEY, ATTR_TYPE as ATTR_TYPE, ATTR_VALUE as ATTR_VALUE, ATTR_VALUE_RAW as ATTR_VALUE_RAW, DOMAIN as DOMAIN, ZWAVE_JS_NOTIFICATION_EVENT as ZWAVE_JS_NOTIFICATION_EVENT, ZWAVE_JS_VALUE_NOTIFICATION_EVENT as ZWAVE_JS_VALUE_NOTIFICATION_EVENT
from .helpers import async_get_node_from_device_id as async_get_node_from_device_id, async_get_node_status_sensor_entity_id as async_get_node_status_sensor_entity_id, async_is_device_config_entry_not_loaded as async_is_device_config_entry_not_loaded, check_type_schema_map as check_type_schema_map, copy_available_params as copy_available_params, get_value_state_schema as get_value_state_schema, get_zwave_value_from_config as get_zwave_value_from_config, remove_keys_with_empty_values as remove_keys_with_empty_values
from .triggers.value_updated import ATTR_FROM as ATTR_FROM, ATTR_TO as ATTR_TO
from homeassistant.components.automation import AutomationActionType as AutomationActionType
from homeassistant.components.device_automation import DEVICE_TRIGGER_BASE_SCHEMA as DEVICE_TRIGGER_BASE_SCHEMA
from homeassistant.components.device_automation.exceptions import InvalidDeviceAutomationConfig as InvalidDeviceAutomationConfig
from homeassistant.components.homeassistant.triggers import event as event, state as state
from homeassistant.const import CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_DOMAIN as CONF_DOMAIN, CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_PLATFORM as CONF_PLATFORM, CONF_TYPE as CONF_TYPE
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import device_registry as device_registry, entity_registry as entity_registry
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any

CONF_SUBTYPE: str
ENTRY_CONTROL_NOTIFICATION: str
NOTIFICATION_NOTIFICATION: str
BASIC_VALUE_NOTIFICATION: str
CENTRAL_SCENE_VALUE_NOTIFICATION: str
SCENE_ACTIVATION_VALUE_NOTIFICATION: str
CONFIG_PARAMETER_VALUE_UPDATED: Any
VALUE_VALUE_UPDATED: Any
NODE_STATUS: str
VALUE_SCHEMA: Any
NOTIFICATION_EVENT_CC_MAPPINGS: Any
BASE_EVENT_SCHEMA: Any
NOTIFICATION_NOTIFICATION_SCHEMA: Any
ENTRY_CONTROL_NOTIFICATION_SCHEMA: Any
BASE_VALUE_NOTIFICATION_EVENT_SCHEMA: Any
BASIC_VALUE_NOTIFICATION_SCHEMA: Any
CENTRAL_SCENE_VALUE_NOTIFICATION_SCHEMA: Any
SCENE_ACTIVATION_VALUE_NOTIFICATION_SCHEMA: Any
BASE_STATE_SCHEMA: Any
NODE_STATUSES: Any
NODE_STATUS_SCHEMA: Any
BASE_VALUE_UPDATED_SCHEMA: Any
CONFIG_PARAMETER_VALUE_UPDATED_SCHEMA: Any
VALUE_VALUE_UPDATED_SCHEMA: Any
TYPE_SCHEMA_MAP: Any
TRIGGER_TYPE_SCHEMA: Any
TRIGGER_SCHEMA: Any

async def async_validate_trigger_config(hass: HomeAssistant, config: ConfigType) -> ConfigType: ...
def get_trigger_platform_from_type(trigger_type: str) -> str: ...
async def async_get_triggers(hass: HomeAssistant, device_id: str) -> list[dict[str, Any]]: ...
async def async_attach_trigger(hass: HomeAssistant, config: ConfigType, action: AutomationActionType, automation_info: dict) -> CALLBACK_TYPE: ...
async def async_get_trigger_capabilities(hass: HomeAssistant, config: ConfigType) -> dict[str, vol.Schema]: ...

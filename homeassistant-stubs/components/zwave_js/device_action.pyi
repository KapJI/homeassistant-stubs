import voluptuous as vol
from .const import ATTR_COMMAND_CLASS as ATTR_COMMAND_CLASS, ATTR_CONFIG_PARAMETER as ATTR_CONFIG_PARAMETER, ATTR_CONFIG_PARAMETER_BITMASK as ATTR_CONFIG_PARAMETER_BITMASK, ATTR_ENDPOINT as ATTR_ENDPOINT, ATTR_METER_TYPE as ATTR_METER_TYPE, ATTR_PROPERTY as ATTR_PROPERTY, ATTR_PROPERTY_KEY as ATTR_PROPERTY_KEY, ATTR_REFRESH_ALL_VALUES as ATTR_REFRESH_ALL_VALUES, ATTR_VALUE as ATTR_VALUE, ATTR_WAIT_FOR_RESULT as ATTR_WAIT_FOR_RESULT, DOMAIN as DOMAIN, SERVICE_CLEAR_LOCK_USERCODE as SERVICE_CLEAR_LOCK_USERCODE, SERVICE_PING as SERVICE_PING, SERVICE_REFRESH_VALUE as SERVICE_REFRESH_VALUE, SERVICE_RESET_METER as SERVICE_RESET_METER, SERVICE_SET_CONFIG_PARAMETER as SERVICE_SET_CONFIG_PARAMETER, SERVICE_SET_LOCK_USERCODE as SERVICE_SET_LOCK_USERCODE, SERVICE_SET_VALUE as SERVICE_SET_VALUE, VALUE_SCHEMA as VALUE_SCHEMA
from .device_automation_helpers import CONF_SUBTYPE as CONF_SUBTYPE, VALUE_ID_REGEX as VALUE_ID_REGEX, generate_config_parameter_subtype as generate_config_parameter_subtype, get_config_parameter_value_schema as get_config_parameter_value_schema
from .helpers import async_get_node_from_device_id as async_get_node_from_device_id
from homeassistant.const import ATTR_DEVICE_ID as ATTR_DEVICE_ID, ATTR_DOMAIN as ATTR_DOMAIN, CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_DOMAIN as CONF_DOMAIN, CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_TYPE as CONF_TYPE, STATE_UNAVAILABLE as STATE_UNAVAILABLE
from homeassistant.core import Context as Context, HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import entity_registry as entity_registry
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any

ACTION_TYPES: Any
CLEAR_LOCK_USERCODE_SCHEMA: Any
PING_SCHEMA: Any
REFRESH_VALUE_SCHEMA: Any
RESET_METER_SCHEMA: Any
SET_CONFIG_PARAMETER_SCHEMA: Any
SET_LOCK_USERCODE_SCHEMA: Any
SET_VALUE_SCHEMA: Any
ACTION_SCHEMA: Any

async def async_get_actions(hass: HomeAssistant, device_id: str) -> list[dict]: ...
async def async_call_action_from_config(hass: HomeAssistant, config: dict, variables: dict, context: Union[Context, None]) -> None: ...
async def async_get_action_capabilities(hass: HomeAssistant, config: ConfigType) -> dict[str, vol.Schema]: ...

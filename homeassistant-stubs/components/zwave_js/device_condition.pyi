import voluptuous as vol
from . import DOMAIN as DOMAIN
from .const import ATTR_COMMAND_CLASS as ATTR_COMMAND_CLASS, ATTR_ENDPOINT as ATTR_ENDPOINT, ATTR_PROPERTY as ATTR_PROPERTY, ATTR_PROPERTY_KEY as ATTR_PROPERTY_KEY, ATTR_VALUE as ATTR_VALUE
from .helpers import async_get_node_from_device_id as async_get_node_from_device_id, get_zwave_value_from_config as get_zwave_value_from_config
from homeassistant.const import CONF_CONDITION as CONF_CONDITION, CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_DOMAIN as CONF_DOMAIN, CONF_TYPE as CONF_TYPE
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import condition as condition
from homeassistant.helpers.config_validation import DEVICE_CONDITION_BASE_SCHEMA as DEVICE_CONDITION_BASE_SCHEMA
from homeassistant.helpers.typing import ConfigType as ConfigType, TemplateVarsType as TemplateVarsType
from typing import Any

CONF_SUBTYPE: str
CONF_VALUE_ID: str
CONF_STATUS: str
NODE_STATUS_TYPE: str
NODE_STATUS_TYPES: Any
CONFIG_PARAMETER_TYPE: str
VALUE_TYPE: str
CONDITION_TYPES: Any
NODE_STATUS_CONDITION_SCHEMA: Any
CONFIG_PARAMETER_CONDITION_SCHEMA: Any
VALUE_CONDITION_SCHEMA: Any
CONDITION_SCHEMA: Any

async def async_validate_condition_config(hass: HomeAssistant, config: ConfigType) -> ConfigType: ...
async def async_get_conditions(hass: HomeAssistant, device_id: str) -> list[dict[str, str]]: ...
def async_condition_from_config(config: ConfigType, config_validation: bool) -> condition.ConditionCheckerType: ...
async def async_get_condition_capabilities(hass: HomeAssistant, config: ConfigType) -> dict[str, vol.Schema]: ...

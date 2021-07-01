from . import DOMAIN as DOMAIN, SUPPORT_CLOSE as SUPPORT_CLOSE, SUPPORT_OPEN as SUPPORT_OPEN, SUPPORT_SET_POSITION as SUPPORT_SET_POSITION, SUPPORT_SET_TILT_POSITION as SUPPORT_SET_TILT_POSITION
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, CONF_ABOVE as CONF_ABOVE, CONF_BELOW as CONF_BELOW, CONF_CONDITION as CONF_CONDITION, CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_DOMAIN as CONF_DOMAIN, CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_TYPE as CONF_TYPE, STATE_CLOSED as STATE_CLOSED, STATE_CLOSING as STATE_CLOSING, STATE_OPEN as STATE_OPEN, STATE_OPENING as STATE_OPENING
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import condition as condition, entity_registry as entity_registry, template as template
from homeassistant.helpers.config_validation import DEVICE_CONDITION_BASE_SCHEMA as DEVICE_CONDITION_BASE_SCHEMA
from homeassistant.helpers.entity import get_supported_features as get_supported_features
from homeassistant.helpers.typing import ConfigType as ConfigType, TemplateVarsType as TemplateVarsType
from typing import Any

POSITION_CONDITION_TYPES: Any
STATE_CONDITION_TYPES: Any
POSITION_CONDITION_SCHEMA: Any
STATE_CONDITION_SCHEMA: Any
CONDITION_SCHEMA: Any

async def async_get_conditions(hass: HomeAssistant, device_id: str) -> list[dict]: ...
async def async_get_condition_capabilities(hass: HomeAssistant, config: dict) -> dict: ...
def async_condition_from_config(config: ConfigType, config_validation: bool) -> condition.ConditionCheckerType: ...

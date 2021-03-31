from . import DOMAIN as DOMAIN
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, CONF_CONDITION as CONF_CONDITION, CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_DOMAIN as CONF_DOMAIN, CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_TYPE as CONF_TYPE, STATE_LOCKED as STATE_LOCKED, STATE_UNLOCKED as STATE_UNLOCKED
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import condition as condition, entity_registry as entity_registry
from homeassistant.helpers.config_validation import DEVICE_CONDITION_BASE_SCHEMA as DEVICE_CONDITION_BASE_SCHEMA
from homeassistant.helpers.typing import ConfigType as ConfigType, TemplateVarsType as TemplateVarsType
from typing import Any

CONDITION_TYPES: Any
CONDITION_SCHEMA: Any

async def async_get_conditions(hass: HomeAssistant, device_id: str) -> list[dict]: ...
def async_condition_from_config(config: ConfigType, config_validation: bool) -> condition.ConditionCheckerType: ...

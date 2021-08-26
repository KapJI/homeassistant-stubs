import voluptuous as vol
from .const import ATTR_OPTIONS as ATTR_OPTIONS, CONF_OPTION as CONF_OPTION, DOMAIN as DOMAIN
from homeassistant.const import CONF_CONDITION as CONF_CONDITION, CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_DOMAIN as CONF_DOMAIN, CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_FOR as CONF_FOR, CONF_TYPE as CONF_TYPE
from homeassistant.core import HomeAssistant as HomeAssistant, HomeAssistantError as HomeAssistantError, callback as callback
from homeassistant.helpers import condition as condition, entity_registry as entity_registry
from homeassistant.helpers.config_validation import DEVICE_CONDITION_BASE_SCHEMA as DEVICE_CONDITION_BASE_SCHEMA
from homeassistant.helpers.entity import get_capability as get_capability
from homeassistant.helpers.typing import ConfigType as ConfigType, TemplateVarsType as TemplateVarsType
from typing import Any

CONDITION_TYPES: Any
CONDITION_SCHEMA: Any

async def async_get_conditions(hass: HomeAssistant, device_id: str) -> list[dict[str, str]]: ...
def async_condition_from_config(config: ConfigType, config_validation: bool) -> condition.ConditionCheckerType: ...
async def async_get_condition_capabilities(hass: HomeAssistant, config: ConfigType) -> dict[str, vol.Schema]: ...

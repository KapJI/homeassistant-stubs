from . import DOMAIN as DOMAIN, STATE_CLEANING as STATE_CLEANING, STATE_DOCKED as STATE_DOCKED, STATE_RETURNING as STATE_RETURNING
from _typeshed import Incomplete
from homeassistant.const import CONF_CONDITION as CONF_CONDITION, CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_DOMAIN as CONF_DOMAIN, CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_TYPE as CONF_TYPE
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import condition as condition
from homeassistant.helpers.config_validation import DEVICE_CONDITION_BASE_SCHEMA as DEVICE_CONDITION_BASE_SCHEMA
from homeassistant.helpers.typing import ConfigType as ConfigType, TemplateVarsType as TemplateVarsType

CONDITION_TYPES: Incomplete
CONDITION_SCHEMA: Incomplete

async def async_get_conditions(hass: HomeAssistant, device_id: str) -> list[dict[str, str]]: ...
def async_condition_from_config(hass: HomeAssistant, config: ConfigType) -> condition.ConditionCheckerType: ...

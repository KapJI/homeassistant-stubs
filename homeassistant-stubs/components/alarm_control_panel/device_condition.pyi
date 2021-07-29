from . import DOMAIN as DOMAIN
from .const import CONDITION_ARMED_AWAY as CONDITION_ARMED_AWAY, CONDITION_ARMED_CUSTOM_BYPASS as CONDITION_ARMED_CUSTOM_BYPASS, CONDITION_ARMED_HOME as CONDITION_ARMED_HOME, CONDITION_ARMED_NIGHT as CONDITION_ARMED_NIGHT, CONDITION_ARMED_VACATION as CONDITION_ARMED_VACATION, CONDITION_DISARMED as CONDITION_DISARMED, CONDITION_TRIGGERED as CONDITION_TRIGGERED
from homeassistant.components.alarm_control_panel.const import SUPPORT_ALARM_ARM_AWAY as SUPPORT_ALARM_ARM_AWAY, SUPPORT_ALARM_ARM_CUSTOM_BYPASS as SUPPORT_ALARM_ARM_CUSTOM_BYPASS, SUPPORT_ALARM_ARM_HOME as SUPPORT_ALARM_ARM_HOME, SUPPORT_ALARM_ARM_NIGHT as SUPPORT_ALARM_ARM_NIGHT, SUPPORT_ALARM_ARM_VACATION as SUPPORT_ALARM_ARM_VACATION
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, CONF_CONDITION as CONF_CONDITION, CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_DOMAIN as CONF_DOMAIN, CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_TYPE as CONF_TYPE, STATE_ALARM_ARMED_AWAY as STATE_ALARM_ARMED_AWAY, STATE_ALARM_ARMED_CUSTOM_BYPASS as STATE_ALARM_ARMED_CUSTOM_BYPASS, STATE_ALARM_ARMED_HOME as STATE_ALARM_ARMED_HOME, STATE_ALARM_ARMED_NIGHT as STATE_ALARM_ARMED_NIGHT, STATE_ALARM_ARMED_VACATION as STATE_ALARM_ARMED_VACATION, STATE_ALARM_DISARMED as STATE_ALARM_DISARMED, STATE_ALARM_TRIGGERED as STATE_ALARM_TRIGGERED
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import condition as condition, entity_registry as entity_registry
from homeassistant.helpers.config_validation import DEVICE_CONDITION_BASE_SCHEMA as DEVICE_CONDITION_BASE_SCHEMA
from homeassistant.helpers.entity import get_supported_features as get_supported_features
from homeassistant.helpers.typing import ConfigType as ConfigType, TemplateVarsType as TemplateVarsType
from typing import Any, Final

CONDITION_TYPES: Final[set[str]]
CONDITION_SCHEMA: Final[Any]

async def async_get_conditions(hass: HomeAssistant, device_id: str) -> list[dict[str, str]]: ...
def async_condition_from_config(config: ConfigType, config_validation: bool) -> condition.ConditionCheckerType: ...

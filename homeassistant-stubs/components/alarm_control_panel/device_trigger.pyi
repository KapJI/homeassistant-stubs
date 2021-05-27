import voluptuous as vol
from . import DOMAIN as DOMAIN
from homeassistant.components.alarm_control_panel.const import SUPPORT_ALARM_ARM_AWAY as SUPPORT_ALARM_ARM_AWAY, SUPPORT_ALARM_ARM_HOME as SUPPORT_ALARM_ARM_HOME, SUPPORT_ALARM_ARM_NIGHT as SUPPORT_ALARM_ARM_NIGHT
from homeassistant.components.automation import AutomationActionType as AutomationActionType
from homeassistant.components.device_automation import TRIGGER_BASE_SCHEMA as TRIGGER_BASE_SCHEMA
from homeassistant.const import ATTR_SUPPORTED_FEATURES as ATTR_SUPPORTED_FEATURES, CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_DOMAIN as CONF_DOMAIN, CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_FOR as CONF_FOR, CONF_PLATFORM as CONF_PLATFORM, CONF_TYPE as CONF_TYPE, STATE_ALARM_ARMED_AWAY as STATE_ALARM_ARMED_AWAY, STATE_ALARM_ARMED_HOME as STATE_ALARM_ARMED_HOME, STATE_ALARM_ARMED_NIGHT as STATE_ALARM_ARMED_NIGHT, STATE_ALARM_ARMING as STATE_ALARM_ARMING, STATE_ALARM_DISARMED as STATE_ALARM_DISARMED, STATE_ALARM_TRIGGERED as STATE_ALARM_TRIGGERED
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant
from homeassistant.helpers import entity_registry as entity_registry
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any, Final

BASIC_TRIGGER_TYPES: Final[set[str]]
TRIGGER_TYPES: Final[set[str]]
TRIGGER_SCHEMA: Final[Any]

async def async_get_triggers(hass: HomeAssistant, device_id: str) -> list[dict[str, str]]: ...
async def async_get_trigger_capabilities(hass: HomeAssistant, config: ConfigType) -> dict[str, vol.Schema]: ...
async def async_attach_trigger(hass: HomeAssistant, config: ConfigType, action: AutomationActionType, automation_info: dict) -> CALLBACK_TYPE: ...

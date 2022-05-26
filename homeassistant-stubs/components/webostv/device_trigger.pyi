from . import trigger as trigger
from .const import DOMAIN as DOMAIN
from .helpers import async_get_client_wrapper_by_device_entry as async_get_client_wrapper_by_device_entry, async_get_device_entry_by_device_id as async_get_device_entry_by_device_id, async_is_device_config_entry_not_loaded as async_is_device_config_entry_not_loaded
from _typeshed import Incomplete
from homeassistant.components.automation import AutomationActionType as AutomationActionType, AutomationTriggerInfo as AutomationTriggerInfo
from homeassistant.components.device_automation import DEVICE_TRIGGER_BASE_SCHEMA as DEVICE_TRIGGER_BASE_SCHEMA
from homeassistant.components.device_automation.exceptions import InvalidDeviceAutomationConfig as InvalidDeviceAutomationConfig
from homeassistant.const import CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_DOMAIN as CONF_DOMAIN, CONF_PLATFORM as CONF_PLATFORM, CONF_TYPE as CONF_TYPE
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.typing import ConfigType as ConfigType

TRIGGER_TYPES: Incomplete
TRIGGER_SCHEMA: Incomplete

async def async_validate_trigger_config(hass: HomeAssistant, config: ConfigType) -> ConfigType: ...
async def async_get_triggers(_hass: HomeAssistant, device_id: str) -> list[dict[str, str]]: ...
async def async_attach_trigger(hass: HomeAssistant, config: ConfigType, action: AutomationActionType, automation_info: AutomationTriggerInfo) -> CALLBACK_TYPE: ...

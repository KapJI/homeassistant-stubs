from .const import DATA_DEVICE_MANAGER as DATA_DEVICE_MANAGER, DOMAIN as DOMAIN
from .events import DEVICE_TRAIT_TRIGGER_MAP as DEVICE_TRAIT_TRIGGER_MAP, NEST_EVENT as NEST_EVENT
from _typeshed import Incomplete
from google_nest_sdm.device_manager import DeviceManager as DeviceManager
from homeassistant.components.automation import AutomationActionType as AutomationActionType, AutomationTriggerInfo as AutomationTriggerInfo
from homeassistant.components.device_automation import DEVICE_TRIGGER_BASE_SCHEMA as DEVICE_TRIGGER_BASE_SCHEMA
from homeassistant.components.device_automation.exceptions import InvalidDeviceAutomationConfig as InvalidDeviceAutomationConfig
from homeassistant.const import CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_DOMAIN as CONF_DOMAIN, CONF_PLATFORM as CONF_PLATFORM, CONF_TYPE as CONF_TYPE
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.typing import ConfigType as ConfigType

DEVICE: str
TRIGGER_TYPES: Incomplete
TRIGGER_SCHEMA: Incomplete

def async_get_nest_device_id(hass: HomeAssistant, device_id: str) -> Union[str, None]: ...
def async_get_device_trigger_types(hass: HomeAssistant, nest_device_id: str) -> list[str]: ...
async def async_get_triggers(hass: HomeAssistant, device_id: str) -> list[dict[str, str]]: ...
async def async_attach_trigger(hass: HomeAssistant, config: ConfigType, action: AutomationActionType, automation_info: AutomationTriggerInfo) -> CALLBACK_TYPE: ...

from .const import DATA_SUBSCRIBER as DATA_SUBSCRIBER, DOMAIN as DOMAIN
from .events import DEVICE_TRAIT_TRIGGER_MAP as DEVICE_TRAIT_TRIGGER_MAP, NEST_EVENT as NEST_EVENT
from homeassistant.components.automation import AutomationActionType as AutomationActionType
from homeassistant.components.device_automation import DEVICE_TRIGGER_BASE_SCHEMA as DEVICE_TRIGGER_BASE_SCHEMA
from homeassistant.components.device_automation.exceptions import InvalidDeviceAutomationConfig as InvalidDeviceAutomationConfig
from homeassistant.const import CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_DOMAIN as CONF_DOMAIN, CONF_PLATFORM as CONF_PLATFORM, CONF_TYPE as CONF_TYPE
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceRegistry as DeviceRegistry
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any

DEVICE: str
TRIGGER_TYPES: Any
TRIGGER_SCHEMA: Any

async def async_get_nest_device_id(hass: HomeAssistant, device_id: str) -> Union[str, None]: ...
async def async_get_device_trigger_types(hass: HomeAssistant, nest_device_id: str) -> list[str]: ...
async def async_get_triggers(hass: HomeAssistant, device_id: str) -> list[dict]: ...
async def async_attach_trigger(hass: HomeAssistant, config: ConfigType, action: AutomationActionType, automation_info: dict) -> CALLBACK_TYPE: ...

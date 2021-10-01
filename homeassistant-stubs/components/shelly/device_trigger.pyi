from . import get_block_device_wrapper as get_block_device_wrapper, get_rpc_device_wrapper as get_rpc_device_wrapper
from .const import ATTR_CHANNEL as ATTR_CHANNEL, ATTR_CLICK_TYPE as ATTR_CLICK_TYPE, BLOCK_INPUTS_EVENTS_TYPES as BLOCK_INPUTS_EVENTS_TYPES, CONF_SUBTYPE as CONF_SUBTYPE, DOMAIN as DOMAIN, EVENT_SHELLY_CLICK as EVENT_SHELLY_CLICK, INPUTS_EVENTS_SUBTYPES as INPUTS_EVENTS_SUBTYPES, RPC_INPUTS_EVENTS_TYPES as RPC_INPUTS_EVENTS_TYPES, SHBTN_MODELS as SHBTN_MODELS
from .utils import get_block_input_triggers as get_block_input_triggers, get_rpc_input_triggers as get_rpc_input_triggers, get_shbtn_input_triggers as get_shbtn_input_triggers
from homeassistant.components.automation import AutomationActionType as AutomationActionType, AutomationTriggerInfo as AutomationTriggerInfo
from homeassistant.components.device_automation import DEVICE_TRIGGER_BASE_SCHEMA as DEVICE_TRIGGER_BASE_SCHEMA
from homeassistant.components.device_automation.exceptions import InvalidDeviceAutomationConfig as InvalidDeviceAutomationConfig
from homeassistant.const import ATTR_DEVICE_ID as ATTR_DEVICE_ID, CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_DOMAIN as CONF_DOMAIN, CONF_EVENT as CONF_EVENT, CONF_PLATFORM as CONF_PLATFORM, CONF_TYPE as CONF_TYPE
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any, Final

TRIGGER_SCHEMA: Final[Any]

def append_input_triggers(triggers: list[dict[str, Any]], input_triggers: list[tuple[str, str]], device_id: str) -> None: ...
async def async_validate_trigger_config(hass: HomeAssistant, config: dict[str, Any]) -> dict[str, Any]: ...
async def async_get_triggers(hass: HomeAssistant, device_id: str) -> list[dict[str, Any]]: ...
async def async_attach_trigger(hass: HomeAssistant, config: ConfigType, action: AutomationActionType, automation_info: AutomationTriggerInfo) -> CALLBACK_TYPE: ...

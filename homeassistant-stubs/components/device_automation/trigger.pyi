import voluptuous as vol
from . import DEVICE_TRIGGER_BASE_SCHEMA as DEVICE_TRIGGER_BASE_SCHEMA, DeviceAutomationType as DeviceAutomationType, async_get_device_automation_platform as async_get_device_automation_platform
from .exceptions import InvalidDeviceAutomationConfig as InvalidDeviceAutomationConfig
from _typeshed import Incomplete
from homeassistant.const import CONF_DOMAIN as CONF_DOMAIN
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant
from homeassistant.helpers.trigger import TriggerActionType as TriggerActionType, TriggerInfo as TriggerInfo
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any, Protocol

TRIGGER_SCHEMA: Incomplete

class DeviceAutomationTriggerProtocol(Protocol):
    TRIGGER_SCHEMA: vol.Schema
    async def async_validate_trigger_config(self, hass: HomeAssistant, config: ConfigType) -> ConfigType: ...
    async def async_attach_trigger(self, hass: HomeAssistant, config: ConfigType, action: TriggerActionType, trigger_info: TriggerInfo) -> CALLBACK_TYPE: ...
    async def async_get_trigger_capabilities(self, hass: HomeAssistant, config: ConfigType) -> dict[str, vol.Schema]: ...
    async def async_get_triggers(self, hass: HomeAssistant, device_id: str) -> list[dict[str, Any]]: ...

async def async_validate_trigger_config(hass: HomeAssistant, config: ConfigType) -> ConfigType: ...
async def async_attach_trigger(hass: HomeAssistant, config: ConfigType, action: TriggerActionType, trigger_info: TriggerInfo) -> CALLBACK_TYPE: ...

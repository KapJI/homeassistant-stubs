import voluptuous as vol
from . import KNXModule as KNXModule, trigger as trigger
from .const import DOMAIN as DOMAIN
from .project import KNXProject as KNXProject
from .trigger import CONF_KNX_DESTINATION as CONF_KNX_DESTINATION, PLATFORM_TYPE_TRIGGER_TELEGRAM as PLATFORM_TYPE_TRIGGER_TELEGRAM, TELEGRAM_TRIGGER_OPTIONS as TELEGRAM_TRIGGER_OPTIONS, TELEGRAM_TRIGGER_SCHEMA as TELEGRAM_TRIGGER_SCHEMA
from _typeshed import Incomplete
from homeassistant.components.device_automation import DEVICE_TRIGGER_BASE_SCHEMA as DEVICE_TRIGGER_BASE_SCHEMA
from homeassistant.components.device_automation.exceptions import InvalidDeviceAutomationConfig as InvalidDeviceAutomationConfig
from homeassistant.const import CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_DOMAIN as CONF_DOMAIN, CONF_PLATFORM as CONF_PLATFORM, CONF_TYPE as CONF_TYPE
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant
from homeassistant.helpers import selector as selector
from homeassistant.helpers.trigger import TriggerActionType as TriggerActionType, TriggerInfo as TriggerInfo
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any, Final

TRIGGER_TELEGRAM: Final[str]
TRIGGER_SCHEMA: Final[Incomplete]

async def async_get_triggers(hass: HomeAssistant, device_id: str) -> list[dict[str, Any]]: ...
async def async_get_trigger_capabilities(hass: HomeAssistant, config: ConfigType) -> dict[str, vol.Schema]: ...
async def async_attach_trigger(hass: HomeAssistant, config: ConfigType, action: TriggerActionType, trigger_info: TriggerInfo) -> CALLBACK_TYPE: ...

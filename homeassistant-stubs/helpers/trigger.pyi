from .typing import ConfigType as ConfigType, TemplateVarsType as TemplateVarsType
from _typeshed import Incomplete
from collections.abc import Callable
from homeassistant.components.device_automation.trigger import DeviceAutomationTriggerProtocol as DeviceAutomationTriggerProtocol
from homeassistant.const import CONF_ALIAS as CONF_ALIAS, CONF_ENABLED as CONF_ENABLED, CONF_ID as CONF_ID, CONF_PLATFORM as CONF_PLATFORM, CONF_VARIABLES as CONF_VARIABLES
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, Context as Context, HomeAssistant as HomeAssistant, callback as callback, is_callback as is_callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.loader import IntegrationNotFound as IntegrationNotFound, async_get_integration as async_get_integration
from typing import Any, Protocol, TypedDict

_PLATFORM_ALIASES: Incomplete

class TriggerActionType(Protocol):
    async def __call__(self, run_variables: dict[str, Any], context: Union[Context, None] = ...) -> None: ...

class TriggerData(TypedDict):
    id: str
    idx: str
    alias: Union[str, None]

class TriggerInfo(TypedDict):
    domain: str
    name: str
    home_assistant_start: bool
    variables: TemplateVarsType
    trigger_data: TriggerData

async def _async_get_trigger_platform(hass: HomeAssistant, config: ConfigType) -> DeviceAutomationTriggerProtocol: ...
async def async_validate_trigger_config(hass: HomeAssistant, trigger_config: list[ConfigType]) -> list[ConfigType]: ...
def _trigger_action_wrapper(hass: HomeAssistant, action: Callable, conf: ConfigType) -> Callable: ...
async def async_initialize_triggers(hass: HomeAssistant, trigger_config: list[ConfigType], action: Callable, domain: str, name: str, log_cb: Callable, home_assistant_start: bool = ..., variables: TemplateVarsType = ...) -> Union[CALLBACK_TYPE, None]: ...

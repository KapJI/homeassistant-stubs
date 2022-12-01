from .typing import ConfigType as ConfigType, TemplateVarsType as TemplateVarsType
from _typeshed import Incomplete
from collections.abc import Callable, Coroutine
from homeassistant.components.device_automation.trigger import DeviceAutomationTriggerProtocol as DeviceAutomationTriggerProtocol
from homeassistant.const import CONF_ALIAS as CONF_ALIAS, CONF_ENABLED as CONF_ENABLED, CONF_ID as CONF_ID, CONF_PLATFORM as CONF_PLATFORM, CONF_VARIABLES as CONF_VARIABLES
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, Context as Context, HassJob as HassJob, HomeAssistant as HomeAssistant, callback as callback, is_callback as is_callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.loader import IntegrationNotFound as IntegrationNotFound, async_get_integration as async_get_integration
from typing import Any, Protocol, TypedDict

_PLATFORM_ALIASES: Incomplete
DATA_PLUGGABLE_ACTIONS: str

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

class PluggableActionsEntry:
    plugs: set[PluggableAction]
    actions: dict[object, tuple[HassJob[[dict[str, Any], Union[Context, None]], Coroutine[Any, Any, None]], dict[str, Any]]]
    def __init__(self, plugs, actions) -> None: ...

class PluggableAction:
    _entry: Union[PluggableActionsEntry, None]
    _update: Incomplete
    def __init__(self, update: Union[CALLBACK_TYPE, None] = ...) -> None: ...
    def __bool__(self) -> bool: ...
    def async_run_update(self) -> None: ...
    @staticmethod
    def async_get_registry(hass: HomeAssistant) -> dict[tuple, PluggableActionsEntry]: ...
    @staticmethod
    def async_attach_trigger(hass: HomeAssistant, trigger: dict[str, str], action: TriggerActionType, variables: dict[str, Any]) -> CALLBACK_TYPE: ...
    def async_register(self, hass: HomeAssistant, trigger: dict[str, str]) -> CALLBACK_TYPE: ...
    async def async_run(self, hass: HomeAssistant, context: Union[Context, None] = ...) -> None: ...

async def _async_get_trigger_platform(hass: HomeAssistant, config: ConfigType) -> DeviceAutomationTriggerProtocol: ...
async def async_validate_trigger_config(hass: HomeAssistant, trigger_config: list[ConfigType]) -> list[ConfigType]: ...
def _trigger_action_wrapper(hass: HomeAssistant, action: Callable, conf: ConfigType) -> Callable: ...
async def async_initialize_triggers(hass: HomeAssistant, trigger_config: list[ConfigType], action: Callable, domain: str, name: str, log_cb: Callable, home_assistant_start: bool = ..., variables: TemplateVarsType = ...) -> Union[CALLBACK_TYPE, None]: ...

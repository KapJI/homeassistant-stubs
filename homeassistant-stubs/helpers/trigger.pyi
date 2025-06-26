import abc
import voluptuous as vol
from .integration_platform import async_process_integration_platforms as async_process_integration_platforms
from .template import Template as Template
from .typing import ConfigType as ConfigType, TemplateVarsType as TemplateVarsType
from _typeshed import Incomplete
from collections import defaultdict
from collections.abc import Callable, Coroutine, Iterable
from dataclasses import dataclass, field
from homeassistant.const import CONF_ALIAS as CONF_ALIAS, CONF_ENABLED as CONF_ENABLED, CONF_ID as CONF_ID, CONF_PLATFORM as CONF_PLATFORM, CONF_VARIABLES as CONF_VARIABLES
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, Context as Context, HassJob as HassJob, HomeAssistant as HomeAssistant, callback as callback, is_callback as is_callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, TemplateError as TemplateError
from homeassistant.loader import Integration as Integration, IntegrationNotFound as IntegrationNotFound, async_get_integration as async_get_integration, async_get_integrations as async_get_integrations
from homeassistant.util.async_ import create_eager_task as create_eager_task
from homeassistant.util.hass_dict import HassKey as HassKey
from homeassistant.util.yaml import load_yaml_dict as load_yaml_dict
from homeassistant.util.yaml.loader import JSON_TYPE as JSON_TYPE
from typing import Any, Protocol, TypedDict

_LOGGER: Incomplete
_PLATFORM_ALIASES: Incomplete
DATA_PLUGGABLE_ACTIONS: HassKey[defaultdict[tuple, PluggableActionsEntry]]
TRIGGER_DESCRIPTION_CACHE: HassKey[dict[str, dict[str, Any] | None]]
TRIGGER_PLATFORM_SUBSCRIPTIONS: HassKey[list[Callable[[set[str]], Coroutine[Any, Any, None]]]]
TRIGGERS: HassKey[dict[str, str]]
_FIELD_SCHEMA: Incomplete
_TRIGGER_SCHEMA: Incomplete

def starts_with_dot(key: str) -> str: ...

_TRIGGERS_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant) -> None: ...
@callback
def async_subscribe_platform_events(hass: HomeAssistant, on_event: Callable[[set[str]], Coroutine[Any, Any, None]]) -> Callable[[], None]: ...
async def _register_trigger_platform(hass: HomeAssistant, integration_domain: str, platform: TriggerProtocol) -> None: ...

class Trigger(abc.ABC, metaclass=abc.ABCMeta):
    def __init__(self, hass: HomeAssistant, config: ConfigType) -> None: ...
    @classmethod
    @abc.abstractmethod
    async def async_validate_trigger_config(cls, hass: HomeAssistant, config: ConfigType) -> ConfigType: ...
    @abc.abstractmethod
    async def async_attach_trigger(self, action: TriggerActionType, trigger_info: TriggerInfo) -> CALLBACK_TYPE: ...

class TriggerProtocol(Protocol):
    async def async_get_triggers(self, hass: HomeAssistant) -> dict[str, type[Trigger]]: ...
    TRIGGER_SCHEMA: vol.Schema
    async def async_validate_trigger_config(self, hass: HomeAssistant, config: ConfigType) -> ConfigType: ...
    async def async_attach_trigger(self, hass: HomeAssistant, config: ConfigType, action: TriggerActionType, trigger_info: TriggerInfo) -> CALLBACK_TYPE: ...

class TriggerActionType(Protocol):
    async def __call__(self, run_variables: dict[str, Any], context: Context | None = None) -> Any: ...

class TriggerData(TypedDict):
    id: str
    idx: str
    alias: str | None

class TriggerInfo(TypedDict):
    domain: str
    name: str
    home_assistant_start: bool
    variables: TemplateVarsType
    trigger_data: TriggerData

@dataclass(slots=True)
class PluggableActionsEntry:
    plugs: set[PluggableAction] = field(default_factory=set)
    actions: dict[object, tuple[HassJob[[dict[str, Any], Context | None], Coroutine[Any, Any, None]], dict[str, Any]]] = field(default_factory=dict)

class PluggableAction:
    _entry: PluggableActionsEntry | None
    _update: Incomplete
    def __init__(self, update: CALLBACK_TYPE | None = None) -> None: ...
    def __bool__(self) -> bool: ...
    @callback
    def async_run_update(self) -> None: ...
    @staticmethod
    @callback
    def async_get_registry(hass: HomeAssistant) -> dict[tuple, PluggableActionsEntry]: ...
    @staticmethod
    @callback
    def async_attach_trigger(hass: HomeAssistant, trigger: dict[str, str], action: TriggerActionType, variables: dict[str, Any]) -> CALLBACK_TYPE: ...
    @callback
    def async_register(self, hass: HomeAssistant, trigger: dict[str, str]) -> CALLBACK_TYPE: ...
    async def async_run(self, hass: HomeAssistant, context: Context | None = None) -> None: ...

async def _async_get_trigger_platform(hass: HomeAssistant, config: ConfigType) -> TriggerProtocol: ...
async def async_validate_trigger_config(hass: HomeAssistant, trigger_config: list[ConfigType]) -> list[ConfigType]: ...
def _trigger_action_wrapper(hass: HomeAssistant, action: Callable, conf: ConfigType) -> Callable: ...
async def async_initialize_triggers(hass: HomeAssistant, trigger_config: list[ConfigType], action: Callable, domain: str, name: str, log_cb: Callable, home_assistant_start: bool = False, variables: TemplateVarsType = None) -> CALLBACK_TYPE | None: ...
def _load_triggers_file(hass: HomeAssistant, integration: Integration) -> JSON_TYPE: ...
def _load_triggers_files(hass: HomeAssistant, integrations: Iterable[Integration]) -> dict[str, JSON_TYPE]: ...
async def async_get_all_descriptions(hass: HomeAssistant) -> dict[str, dict[str, Any] | None]: ...

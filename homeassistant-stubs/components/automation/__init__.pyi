from .config import AutomationConfig as AutomationConfig, async_validate_config_item as async_validate_config_item
from .const import CONF_ACTION as CONF_ACTION, CONF_INITIAL_STATE as CONF_INITIAL_STATE, CONF_TRACE as CONF_TRACE, CONF_TRIGGER as CONF_TRIGGER, CONF_TRIGGER_VARIABLES as CONF_TRIGGER_VARIABLES, DEFAULT_INITIAL_STATE as DEFAULT_INITIAL_STATE, DOMAIN as DOMAIN, LOGGER as LOGGER
from .helpers import async_get_blueprints as async_get_blueprints
from .trace import trace_automation as trace_automation
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable
from homeassistant.components import blueprint as blueprint
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, ATTR_MODE as ATTR_MODE, ATTR_NAME as ATTR_NAME, CONF_ALIAS as CONF_ALIAS, CONF_CONDITION as CONF_CONDITION, CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_EVENT_DATA as CONF_EVENT_DATA, CONF_ID as CONF_ID, CONF_MODE as CONF_MODE, CONF_PLATFORM as CONF_PLATFORM, CONF_VARIABLES as CONF_VARIABLES, CONF_ZONE as CONF_ZONE, EVENT_HOMEASSISTANT_STARTED as EVENT_HOMEASSISTANT_STARTED, SERVICE_RELOAD as SERVICE_RELOAD, SERVICE_TOGGLE as SERVICE_TOGGLE, SERVICE_TURN_OFF as SERVICE_TURN_OFF, SERVICE_TURN_ON as SERVICE_TURN_ON, STATE_ON as STATE_ON
from homeassistant.core import Context as Context, CoreState as CoreState, HomeAssistant as HomeAssistant, callback as callback, split_entity_id as split_entity_id
from homeassistant.exceptions import ConditionError as ConditionError, ConditionErrorContainer as ConditionErrorContainer, ConditionErrorIndex as ConditionErrorIndex, HomeAssistantError as HomeAssistantError, TemplateError as TemplateError
from homeassistant.helpers import condition as condition, extract_domain_configs as extract_domain_configs
from homeassistant.helpers.entity import ToggleEntity as ToggleEntity
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.integration_platform import async_process_integration_platform_for_component as async_process_integration_platform_for_component
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from homeassistant.helpers.script import ATTR_CUR as ATTR_CUR, ATTR_MAX as ATTR_MAX, CONF_MAX as CONF_MAX, CONF_MAX_EXCEEDED as CONF_MAX_EXCEEDED, Script as Script, script_stack_cv as script_stack_cv
from homeassistant.helpers.script_variables import ScriptVariables as ScriptVariables
from homeassistant.helpers.service import ReloadServiceHelper as ReloadServiceHelper, async_register_admin_service as async_register_admin_service
from homeassistant.helpers.trace import TraceElement as TraceElement, script_execution_set as script_execution_set, trace_append_element as trace_append_element, trace_get as trace_get, trace_path as trace_path
from homeassistant.helpers.trigger import async_initialize_triggers as async_initialize_triggers
from homeassistant.helpers.typing import ConfigType as ConfigType, TemplateVarsType as TemplateVarsType
from homeassistant.loader import bind_hass as bind_hass
from homeassistant.util.dt import parse_datetime as parse_datetime
from typing import Any, TypedDict

ENTITY_ID_FORMAT: Incomplete
CONF_SKIP_CONDITION: str
CONF_STOP_ACTIONS: str
DEFAULT_STOP_ACTIONS: bool
EVENT_AUTOMATION_RELOADED: str
EVENT_AUTOMATION_TRIGGERED: str
ATTR_LAST_TRIGGERED: str
ATTR_SOURCE: str
ATTR_VARIABLES: str
SERVICE_TRIGGER: str
_LOGGER: Incomplete
AutomationActionType = Callable[[HomeAssistant, TemplateVarsType], Awaitable[None]]

class AutomationTriggerData(TypedDict):
    id: str
    idx: str

class AutomationTriggerInfo(TypedDict):
    domain: str
    name: str
    home_assistant_start: bool
    variables: TemplateVarsType
    trigger_data: AutomationTriggerData

def is_on(hass, entity_id): ...
def automations_with_entity(hass: HomeAssistant, entity_id: str) -> list[str]: ...
def entities_in_automation(hass: HomeAssistant, entity_id: str) -> list[str]: ...
def automations_with_device(hass: HomeAssistant, device_id: str) -> list[str]: ...
def devices_in_automation(hass: HomeAssistant, entity_id: str) -> list[str]: ...
def automations_with_area(hass: HomeAssistant, area_id: str) -> list[str]: ...
def areas_in_automation(hass: HomeAssistant, entity_id: str) -> list[str]: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...

class AutomationEntity(ToggleEntity, RestoreEntity):
    _attr_should_poll: bool
    _attr_name: Incomplete
    _trigger_config: Incomplete
    _async_detach_triggers: Incomplete
    _cond_func: Incomplete
    action_script: Incomplete
    _initial_state: Incomplete
    _is_enabled: bool
    _referenced_entities: Incomplete
    _referenced_devices: Incomplete
    _logger: Incomplete
    _variables: Incomplete
    _trigger_variables: Incomplete
    _raw_config: Incomplete
    _blueprint_inputs: Incomplete
    _trace_config: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, automation_id, name, trigger_config, cond_func, action_script, initial_state, variables, trigger_variables, raw_config, blueprint_inputs, trace_config) -> None: ...
    @property
    def extra_state_attributes(self): ...
    @property
    def is_on(self) -> bool: ...
    @property
    def referenced_areas(self): ...
    @property
    def referenced_devices(self): ...
    @property
    def referenced_entities(self): ...
    async def async_added_to_hass(self) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_trigger(self, run_variables, context: Incomplete | None = ..., skip_condition: bool = ...) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    async def async_enable(self) -> None: ...
    async def async_disable(self, stop_actions=...) -> None: ...
    async def _async_attach_triggers(self, home_assistant_start: bool) -> Union[Callable[[], None], None]: ...

async def _async_process_config(hass: HomeAssistant, config: dict[str, Any], component: EntityComponent) -> bool: ...
async def _async_process_if(hass, name, config, p_config): ...
def _trigger_extract_device(trigger_conf: dict) -> list[str]: ...
def _trigger_extract_entities(trigger_conf: dict) -> list[str]: ...

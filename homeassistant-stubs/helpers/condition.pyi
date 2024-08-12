import voluptuous as vol
from .sun import get_astral_event_date as get_astral_event_date
from .template import Template as Template, render_complex as render_complex
from .trace import TraceElement as TraceElement, trace_append_element as trace_append_element, trace_path as trace_path, trace_path_get as trace_path_get, trace_stack_cv as trace_stack_cv, trace_stack_pop as trace_stack_pop, trace_stack_push as trace_stack_push, trace_stack_top as trace_stack_top
from .typing import ConfigType as ConfigType, TemplateVarsType as TemplateVarsType
from _typeshed import Incomplete
from collections.abc import Callable, Container, Generator
from datetime import time as dt_time, timedelta
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass
from homeassistant.const import ATTR_DEVICE_CLASS as ATTR_DEVICE_CLASS, ATTR_GPS_ACCURACY as ATTR_GPS_ACCURACY, ATTR_LATITUDE as ATTR_LATITUDE, ATTR_LONGITUDE as ATTR_LONGITUDE, CONF_ABOVE as CONF_ABOVE, CONF_AFTER as CONF_AFTER, CONF_ATTRIBUTE as CONF_ATTRIBUTE, CONF_BEFORE as CONF_BEFORE, CONF_BELOW as CONF_BELOW, CONF_CONDITION as CONF_CONDITION, CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_ENABLED as CONF_ENABLED, CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_FOR as CONF_FOR, CONF_ID as CONF_ID, CONF_MATCH as CONF_MATCH, CONF_STATE as CONF_STATE, CONF_VALUE_TEMPLATE as CONF_VALUE_TEMPLATE, CONF_WEEKDAY as CONF_WEEKDAY, CONF_ZONE as CONF_ZONE, ENTITY_MATCH_ALL as ENTITY_MATCH_ALL, ENTITY_MATCH_ANY as ENTITY_MATCH_ANY, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN, SUN_EVENT_SUNRISE as SUN_EVENT_SUNRISE, SUN_EVENT_SUNSET as SUN_EVENT_SUNSET, WEEKDAYS as WEEKDAYS
from homeassistant.core import HomeAssistant as HomeAssistant, State as State, callback as callback
from homeassistant.exceptions import ConditionError as ConditionError, ConditionErrorContainer as ConditionErrorContainer, ConditionErrorIndex as ConditionErrorIndex, ConditionErrorMessage as ConditionErrorMessage, HomeAssistantError as HomeAssistantError, TemplateError as TemplateError
from homeassistant.loader import IntegrationNotFound as IntegrationNotFound, async_get_integration as async_get_integration
from homeassistant.util.async_ import run_callback_threadsafe as run_callback_threadsafe
from typing import Any, Protocol

ASYNC_FROM_CONFIG_FORMAT: str
FROM_CONFIG_FORMAT: str
VALIDATE_CONFIG_FORMAT: str
_PLATFORM_ALIASES: Incomplete
INPUT_ENTITY_ID: Incomplete

class ConditionProtocol(Protocol):
    CONDITION_SCHEMA: vol.Schema
    async def async_validate_condition_config(self, hass: HomeAssistant, config: ConfigType) -> ConfigType: ...
    def async_condition_from_config(self, hass: HomeAssistant, config: ConfigType) -> ConditionCheckerType: ...
ConditionCheckerType = Callable[[HomeAssistant, TemplateVarsType], bool | None]

def condition_trace_append(variables: TemplateVarsType, path: str) -> TraceElement: ...
def condition_trace_set_result(result: bool, **kwargs: Any) -> None: ...
def condition_trace_update_result(**kwargs: Any) -> None: ...
def trace_condition(variables: TemplateVarsType) -> Generator[TraceElement]: ...
def trace_condition_function(condition: ConditionCheckerType) -> ConditionCheckerType: ...
async def _async_get_condition_platform(hass: HomeAssistant, config: ConfigType) -> ConditionProtocol | None: ...
async def async_from_config(hass: HomeAssistant, config: ConfigType) -> ConditionCheckerType: ...
async def async_and_from_config(hass: HomeAssistant, config: ConfigType) -> ConditionCheckerType: ...
async def async_or_from_config(hass: HomeAssistant, config: ConfigType) -> ConditionCheckerType: ...
async def async_not_from_config(hass: HomeAssistant, config: ConfigType) -> ConditionCheckerType: ...
def numeric_state(hass: HomeAssistant, entity: str | State | None, below: float | str | None = None, above: float | str | None = None, value_template: Template | None = None, variables: TemplateVarsType = None) -> bool: ...
def async_numeric_state(hass: HomeAssistant, entity: str | State | None, below: float | str | None = None, above: float | str | None = None, value_template: Template | None = None, variables: TemplateVarsType = None, attribute: str | None = None) -> bool: ...
def async_numeric_state_from_config(config: ConfigType) -> ConditionCheckerType: ...
def state(hass: HomeAssistant, entity: str | State | None, req_state: Any, for_period: timedelta | None = None, attribute: str | None = None, variables: TemplateVarsType = None) -> bool: ...
def state_from_config(config: ConfigType) -> ConditionCheckerType: ...
def sun(hass: HomeAssistant, before: str | None = None, after: str | None = None, before_offset: timedelta | None = None, after_offset: timedelta | None = None) -> bool: ...
def sun_from_config(config: ConfigType) -> ConditionCheckerType: ...
def template(hass: HomeAssistant, value_template: Template, variables: TemplateVarsType = None) -> bool: ...
def async_template(hass: HomeAssistant, value_template: Template, variables: TemplateVarsType = None, trace_result: bool = True) -> bool: ...
def async_template_from_config(config: ConfigType) -> ConditionCheckerType: ...
def time(hass: HomeAssistant, before: dt_time | str | None = None, after: dt_time | str | None = None, weekday: str | Container[str] | None = None) -> bool: ...
def time_from_config(config: ConfigType) -> ConditionCheckerType: ...
def zone(hass: HomeAssistant, zone_ent: str | State | None, entity: str | State | None) -> bool: ...
def zone_from_config(config: ConfigType) -> ConditionCheckerType: ...
async def async_trigger_from_config(hass: HomeAssistant, config: ConfigType) -> ConditionCheckerType: ...
def numeric_state_validate_config(hass: HomeAssistant, config: ConfigType) -> ConfigType: ...
def state_validate_config(hass: HomeAssistant, config: ConfigType) -> ConfigType: ...
async def async_validate_condition_config(hass: HomeAssistant, config: ConfigType) -> ConfigType: ...
async def async_validate_conditions_config(hass: HomeAssistant, conditions: list[ConfigType]) -> list[ConfigType | Template]: ...
def async_extract_entities(config: ConfigType | Template) -> set[str]: ...
def async_extract_devices(config: ConfigType | Template) -> set[str]: ...

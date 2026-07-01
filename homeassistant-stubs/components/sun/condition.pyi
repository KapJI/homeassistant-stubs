import abc
import voluptuous as vol
from .const import DOMAIN as DOMAIN, ELEVATION_ASTRONOMICAL as ELEVATION_ASTRONOMICAL, ELEVATION_CIVIL as ELEVATION_CIVIL, ELEVATION_HORIZON as ELEVATION_HORIZON, ELEVATION_NAUTICAL as ELEVATION_NAUTICAL, STATE_ATTR_ELEVATION as STATE_ATTR_ELEVATION
from _typeshed import Incomplete
from datetime import timedelta
from homeassistant.const import CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_OPTIONS as CONF_OPTIONS, CONF_TARGET as CONF_TARGET, CONF_TYPE as CONF_TYPE, DEGREE as DEGREE, SUN_EVENT_SUNRISE as SUN_EVENT_SUNRISE, SUN_EVENT_SUNSET as SUN_EVENT_SUNSET
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.automation import DomainSpec as DomainSpec, move_top_level_schema_fields_to_options as move_top_level_schema_fields_to_options
from homeassistant.helpers.condition import ATTR_BEHAVIOR as ATTR_BEHAVIOR, BEHAVIOR_ANY as BEHAVIOR_ANY, Condition as Condition, ConditionCheckParams as ConditionCheckParams, ConditionConfig as ConditionConfig, EntityNumericalConditionBase as EntityNumericalConditionBase, condition_trace_set_result as condition_trace_set_result, condition_trace_update_result as condition_trace_update_result
from homeassistant.helpers.selector import NumericThresholdMode as NumericThresholdMode, NumericThresholdSelector as NumericThresholdSelector, NumericThresholdSelectorConfig as NumericThresholdSelectorConfig
from homeassistant.helpers.sun import get_astral_event_date as get_astral_event_date, get_astral_observer as get_astral_observer, is_up as is_up
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any, Unpack, override

_OPTIONS_SCHEMA_DICT: dict[vol.Marker, Any]
_CONDITION_SCHEMA: Incomplete

def sun(hass: HomeAssistant, before: str | None = None, after: str | None = None, before_offset: timedelta | None = None, after_offset: timedelta | None = None) -> bool: ...

class SunCondition(Condition):
    _options: dict[str, Any]
    @classmethod
    @override
    async def async_validate_complete_config(cls, hass: HomeAssistant, complete_config: ConfigType) -> ConfigType: ...
    @classmethod
    @override
    async def async_validate_config(cls, hass: HomeAssistant, config: ConfigType) -> ConfigType: ...
    _before: Incomplete
    _after: Incomplete
    _before_offset: Incomplete
    _after_offset: Incomplete
    def __init__(self, hass: HomeAssistant, config: ConditionConfig) -> None: ...
    @override
    def _async_check(self, **kwargs: Unpack[ConditionCheckParams]) -> bool: ...

_STATE_CONDITION_SCHEMA: Incomplete
_SUN_ENTITY_ID: Incomplete
_ELEVATION_DOMAIN_SPECS: Incomplete

def _solar_position(hass: HomeAssistant) -> tuple[float, bool]: ...

class _SunStateCondition(Condition, metaclass=abc.ABCMeta):
    @classmethod
    @override
    async def async_validate_config(cls, hass: HomeAssistant, config: ConfigType) -> ConfigType: ...

class _UpCondition(_SunStateCondition):
    @override
    def _async_check(self, **kwargs: Unpack[ConditionCheckParams]) -> bool: ...

class _SetCondition(_SunStateCondition):
    @override
    def _async_check(self, **kwargs: Unpack[ConditionCheckParams]) -> bool: ...

class _AscendingCondition(_SunStateCondition):
    @override
    def _async_check(self, **kwargs: Unpack[ConditionCheckParams]) -> bool: ...

class _DescendingCondition(_SunStateCondition):
    @override
    def _async_check(self, **kwargs: Unpack[ConditionCheckParams]) -> bool: ...

class _NightCondition(_SunStateCondition):
    @override
    def _async_check(self, **kwargs: Unpack[ConditionCheckParams]) -> bool: ...

_TWILIGHT_ANY: str
_TWILIGHT_CIVIL: str
_TWILIGHT_NAUTICAL: str
_TWILIGHT_ASTRONOMICAL: str
_TWILIGHT_BANDS: Incomplete
_TWILIGHT_CONDITION_SCHEMA: Incomplete

class _TwilightCondition(Condition):
    _rising: bool
    @classmethod
    @override
    async def async_validate_config(cls, hass: HomeAssistant, config: ConfigType) -> ConfigType: ...
    def __init__(self, hass: HomeAssistant, config: ConditionConfig) -> None: ...
    @override
    def _async_check(self, **kwargs: Unpack[ConditionCheckParams]) -> bool: ...

class _MorningTwilightCondition(_TwilightCondition):
    _rising: bool

class _EveningTwilightCondition(_TwilightCondition):
    _rising: bool

_ELEVATION_CONDITION_SCHEMA: Incomplete

class _ElevationCondition(EntityNumericalConditionBase):
    _domain_specs = _ELEVATION_DOMAIN_SPECS
    _valid_unit = DEGREE
    _schema = _ELEVATION_CONDITION_SCHEMA
    @classmethod
    @override
    async def async_validate_config(cls, hass: HomeAssistant, config: ConfigType) -> ConfigType: ...

CONDITIONS: dict[str, type[Condition]]

async def async_get_conditions(hass: HomeAssistant) -> dict[str, type[Condition]]: ...

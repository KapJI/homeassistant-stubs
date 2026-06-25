import voluptuous as vol
from .const import DOMAIN as DOMAIN, ELEVATION_ASTRONOMICAL as ELEVATION_ASTRONOMICAL, ELEVATION_CIVIL as ELEVATION_CIVIL, ELEVATION_NAUTICAL as ELEVATION_NAUTICAL, STATE_ATTR_ELEVATION as STATE_ATTR_ELEVATION
from _typeshed import Incomplete
from datetime import datetime, timedelta
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, CONF_EVENT as CONF_EVENT, CONF_FOR as CONF_FOR, CONF_OFFSET as CONF_OFFSET, CONF_OPTIONS as CONF_OPTIONS, CONF_TYPE as CONF_TYPE, DEGREE as DEGREE, EVENT_CORE_CONFIG_UPDATE as EVENT_CORE_CONFIG_UPDATE, SUN_EVENT_SUNRISE as SUN_EVENT_SUNRISE, SUN_EVENT_SUNSET as SUN_EVENT_SUNSET
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.automation import DomainSpec as DomainSpec, move_top_level_schema_fields_to_options as move_top_level_schema_fields_to_options
from homeassistant.helpers.event import async_track_point_in_utc_time as async_track_point_in_utc_time
from homeassistant.helpers.selector import NumericThresholdMode as NumericThresholdMode, NumericThresholdSelector as NumericThresholdSelector, NumericThresholdSelectorConfig as NumericThresholdSelectorConfig
from homeassistant.helpers.sun import get_astral_event_next as get_astral_event_next, get_astral_observer as get_astral_observer, get_observer_astral_event_next as get_observer_astral_event_next
from homeassistant.helpers.trigger import EntityNumericalStateChangedTriggerBase as EntityNumericalStateChangedTriggerBase, EntityNumericalStateCrossedThresholdTriggerBase as EntityNumericalStateCrossedThresholdTriggerBase, EntityNumericalStateTriggerBase as EntityNumericalStateTriggerBase, Trigger as Trigger, TriggerActionRunner as TriggerActionRunner, TriggerConfig as TriggerConfig, TriggerNotTriggeredReporter as TriggerNotTriggeredReporter
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any, override

_SUN_EVENT_SOLAR_NOON: str
_SUN_EVENT_SOLAR_MIDNIGHT: str
_SUN_EVENT_DAWN: str
_SUN_EVENT_DUSK: str
_TWILIGHT_CIVIL: str
_TWILIGHT_NAUTICAL: str
_TWILIGHT_ASTRONOMICAL: str
_TWILIGHT_ELEVATIONS: Incomplete
_SUN_ENTITY_ID: Incomplete
_ELEVATION_DOMAIN_SPECS: Incomplete
_ELEVATION_CHANGED_TRIGGER_SCHEMA: Incomplete
_ELEVATION_CROSSED_TRIGGER_SCHEMA: Incomplete

class SunElevationTrigger(EntityNumericalStateTriggerBase):
    _domain_specs = _ELEVATION_DOMAIN_SPECS
    _valid_unit = DEGREE
    def __init__(self, hass: HomeAssistant, config: TriggerConfig) -> None: ...

class SunElevationChangedTrigger(SunElevationTrigger, EntityNumericalStateChangedTriggerBase):
    _schema = _ELEVATION_CHANGED_TRIGGER_SCHEMA

class SunElevationCrossedTrigger(SunElevationTrigger, EntityNumericalStateCrossedThresholdTriggerBase):
    _schema = _ELEVATION_CROSSED_TRIGGER_SCHEMA

_EVENT_TRIGGER_SCHEMA: Incomplete

class SunEventTrigger(Trigger):
    _event: str
    _schema: vol.Schema
    @override
    @classmethod
    async def async_validate_config(cls, hass: HomeAssistant, config: ConfigType) -> ConfigType: ...
    _options: Incomplete
    def __init__(self, hass: HomeAssistant, config: TriggerConfig) -> None: ...
    def _get_next_event(self, utc_point_in_time: datetime) -> datetime: ...
    def _action_payload(self) -> dict[str, Any]: ...
    @override
    async def async_attach_runner(self, run_action: TriggerActionRunner, did_not_trigger: TriggerNotTriggeredReporter | None = None) -> CALLBACK_TYPE: ...

class SunriseTrigger(SunEventTrigger):
    _event = SUN_EVENT_SUNRISE

class SunsetTrigger(SunEventTrigger):
    _event = SUN_EVENT_SUNSET

class SolarNoonTrigger(SunEventTrigger):
    _event = _SUN_EVENT_SOLAR_NOON

class SolarMidnightTrigger(SunEventTrigger):
    _event = _SUN_EVENT_SOLAR_MIDNIGHT

_DAWN_DUSK_TRIGGER_SCHEMA: Incomplete

class SunDawnDuskTrigger(SunEventTrigger):
    _schema = _DAWN_DUSK_TRIGGER_SCHEMA
    _twilight: str
    _elevation: Incomplete
    def __init__(self, hass: HomeAssistant, config: TriggerConfig) -> None: ...
    @override
    def _get_next_event(self, utc_point_in_time: datetime) -> datetime: ...
    @override
    def _action_payload(self) -> dict[str, Any]: ...

class DawnTrigger(SunDawnDuskTrigger):
    _event = _SUN_EVENT_DAWN

class DuskTrigger(SunDawnDuskTrigger):
    _event = _SUN_EVENT_DUSK

_LEGACY_OPTIONS_SCHEMA_DICT: dict[vol.Marker, Any]

class LegacySunTrigger(SunEventTrigger):
    _schema: Incomplete
    @override
    @classmethod
    async def async_validate_complete_config(cls, hass: HomeAssistant, complete_config: ConfigType) -> ConfigType: ...
    _event: Incomplete
    _offset: timedelta
    def __init__(self, hass: HomeAssistant, config: TriggerConfig) -> None: ...
    @override
    def _get_next_event(self, utc_point_in_time: datetime) -> datetime: ...
    @override
    def _action_payload(self) -> dict[str, Any]: ...

TRIGGERS: dict[str, type[Trigger]]

async def async_get_triggers(hass: HomeAssistant) -> dict[str, type[Trigger]]: ...

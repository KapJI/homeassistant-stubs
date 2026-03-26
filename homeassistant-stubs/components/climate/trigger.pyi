import abc
from .const import ATTR_HUMIDITY as ATTR_HUMIDITY, ATTR_HVAC_ACTION as ATTR_HVAC_ACTION, DOMAIN as DOMAIN, HVACAction as HVACAction, HVACMode as HVACMode
from _typeshed import Incomplete
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, CONF_OPTIONS as CONF_OPTIONS, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant, State as State
from homeassistant.helpers.automation import DomainSpec as DomainSpec, NumericalDomainSpec as NumericalDomainSpec
from homeassistant.helpers.trigger import ENTITY_STATE_TRIGGER_SCHEMA_FIRST_LAST as ENTITY_STATE_TRIGGER_SCHEMA_FIRST_LAST, EntityNumericalStateChangedTriggerWithUnitBase as EntityNumericalStateChangedTriggerWithUnitBase, EntityNumericalStateCrossedThresholdTriggerWithUnitBase as EntityNumericalStateCrossedThresholdTriggerWithUnitBase, EntityNumericalStateTriggerWithUnitBase as EntityNumericalStateTriggerWithUnitBase, EntityTargetStateTriggerBase as EntityTargetStateTriggerBase, Trigger as Trigger, TriggerConfig as TriggerConfig, make_entity_numerical_state_changed_trigger as make_entity_numerical_state_changed_trigger, make_entity_numerical_state_crossed_threshold_trigger as make_entity_numerical_state_crossed_threshold_trigger, make_entity_target_state_trigger as make_entity_target_state_trigger, make_entity_transition_trigger as make_entity_transition_trigger
from homeassistant.util.unit_conversion import TemperatureConverter as TemperatureConverter

CONF_HVAC_MODE: str
HVAC_MODE_CHANGED_TRIGGER_SCHEMA: Incomplete

class HVACModeChangedTrigger(EntityTargetStateTriggerBase):
    _domain_specs: Incomplete
    _schema = HVAC_MODE_CHANGED_TRIGGER_SCHEMA
    _to_states: Incomplete
    def __init__(self, hass: HomeAssistant, config: TriggerConfig) -> None: ...

class _ClimateTargetTemperatureTriggerMixin(EntityNumericalStateTriggerWithUnitBase, metaclass=abc.ABCMeta):
    _base_unit: Incomplete
    _domain_specs: Incomplete
    _unit_converter = TemperatureConverter
    def _get_entity_unit(self, state: State) -> str | None: ...

class ClimateTargetTemperatureChangedTrigger(_ClimateTargetTemperatureTriggerMixin, EntityNumericalStateChangedTriggerWithUnitBase): ...
class ClimateTargetTemperatureCrossedThresholdTrigger(_ClimateTargetTemperatureTriggerMixin, EntityNumericalStateCrossedThresholdTriggerWithUnitBase): ...

TRIGGERS: dict[str, type[Trigger]]

async def async_get_triggers(hass: HomeAssistant) -> dict[str, type[Trigger]]: ...

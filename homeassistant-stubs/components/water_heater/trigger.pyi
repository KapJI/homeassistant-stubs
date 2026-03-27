import abc
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, CONF_OPTIONS as CONF_OPTIONS, STATE_OFF as STATE_OFF, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant, State as State
from homeassistant.helpers.automation import DomainSpec as DomainSpec
from homeassistant.helpers.trigger import ENTITY_STATE_TRIGGER_SCHEMA_FIRST_LAST as ENTITY_STATE_TRIGGER_SCHEMA_FIRST_LAST, EntityNumericalStateChangedTriggerWithUnitBase as EntityNumericalStateChangedTriggerWithUnitBase, EntityNumericalStateCrossedThresholdTriggerWithUnitBase as EntityNumericalStateCrossedThresholdTriggerWithUnitBase, EntityNumericalStateTriggerWithUnitBase as EntityNumericalStateTriggerWithUnitBase, EntityTargetStateTriggerBase as EntityTargetStateTriggerBase, Trigger as Trigger, TriggerConfig as TriggerConfig, make_entity_origin_state_trigger as make_entity_origin_state_trigger, make_entity_target_state_trigger as make_entity_target_state_trigger
from homeassistant.util.unit_conversion import TemperatureConverter as TemperatureConverter

CONF_OPERATION_MODE: str
_OPERATION_MODE_CHANGED_TRIGGER_SCHEMA: Incomplete

class WaterHeaterOperationModeChangedTrigger(EntityTargetStateTriggerBase):
    _domain_specs: Incomplete
    _schema = _OPERATION_MODE_CHANGED_TRIGGER_SCHEMA
    _to_states: Incomplete
    def __init__(self, hass: HomeAssistant, config: TriggerConfig) -> None: ...

class _WaterHeaterTargetTemperatureTriggerMixin(EntityNumericalStateTriggerWithUnitBase, metaclass=abc.ABCMeta):
    _base_unit: Incomplete
    _domain_specs: Incomplete
    _unit_converter = TemperatureConverter
    def _get_entity_unit(self, state: State) -> str | None: ...

class WaterHeaterTargetTemperatureChangedTrigger(_WaterHeaterTargetTemperatureTriggerMixin, EntityNumericalStateChangedTriggerWithUnitBase): ...
class WaterHeaterTargetTemperatureCrossedThresholdTrigger(_WaterHeaterTargetTemperatureTriggerMixin, EntityNumericalStateCrossedThresholdTriggerWithUnitBase): ...

TRIGGERS: dict[str, type[Trigger]]

async def async_get_triggers(hass: HomeAssistant) -> dict[str, type[Trigger]]: ...

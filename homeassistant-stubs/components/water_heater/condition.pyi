from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, CONF_OPTIONS as CONF_OPTIONS, CONF_TARGET as CONF_TARGET, STATE_OFF as STATE_OFF, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant, State as State
from homeassistant.helpers.automation import DomainSpec as DomainSpec, NumericalDomainSpec as NumericalDomainSpec
from homeassistant.helpers.condition import ATTR_BEHAVIOR as ATTR_BEHAVIOR, BEHAVIOR_ALL as BEHAVIOR_ALL, BEHAVIOR_ANY as BEHAVIOR_ANY, Condition as Condition, ConditionConfig as ConditionConfig, EntityConditionBase as EntityConditionBase, EntityNumericalConditionWithUnitBase as EntityNumericalConditionWithUnitBase, make_entity_state_condition as make_entity_state_condition
from homeassistant.util.unit_conversion import TemperatureConverter as TemperatureConverter

ATTR_OPERATION_MODE: str
_OPERATION_MODE_CONDITION_SCHEMA: Incomplete

class WaterHeaterOnCondition(EntityConditionBase):
    _domain_specs: Incomplete
    def is_valid_state(self, entity_state: State) -> bool: ...

class WaterHeaterOperationModeCondition(EntityConditionBase):
    _domain_specs: Incomplete
    _schema = _OPERATION_MODE_CONDITION_SCHEMA
    _operation_modes: set[str]
    def __init__(self, hass: HomeAssistant, config: ConditionConfig) -> None: ...
    def is_valid_state(self, entity_state: State) -> bool: ...

class WaterHeaterTargetTemperatureCondition(EntityNumericalConditionWithUnitBase):
    _base_unit: Incomplete
    _domain_specs: Incomplete
    _unit_converter = TemperatureConverter
    def _get_entity_unit(self, entity_state: State) -> str | None: ...

CONDITIONS: dict[str, type[Condition]]

async def async_get_conditions(hass: HomeAssistant) -> dict[str, type[Condition]]: ...

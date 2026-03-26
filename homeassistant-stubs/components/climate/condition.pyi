from .const import ATTR_HUMIDITY as ATTR_HUMIDITY, ATTR_HVAC_ACTION as ATTR_HVAC_ACTION, DOMAIN as DOMAIN, HVACAction as HVACAction, HVACMode as HVACMode
from _typeshed import Incomplete
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant, State as State
from homeassistant.helpers.automation import DomainSpec as DomainSpec, NumericalDomainSpec as NumericalDomainSpec
from homeassistant.helpers.condition import Condition as Condition, EntityNumericalConditionWithUnitBase as EntityNumericalConditionWithUnitBase, make_entity_numerical_condition as make_entity_numerical_condition, make_entity_state_condition as make_entity_state_condition
from homeassistant.util.unit_conversion import TemperatureConverter as TemperatureConverter

class ClimateTargetTemperatureCondition(EntityNumericalConditionWithUnitBase):
    _base_unit: Incomplete
    _domain_specs: Incomplete
    _unit_converter = TemperatureConverter
    def _get_entity_unit(self, entity_state: State) -> str | None: ...

CONDITIONS: dict[str, type[Condition]]

async def async_get_conditions(hass: HomeAssistant) -> dict[str, type[Condition]]: ...

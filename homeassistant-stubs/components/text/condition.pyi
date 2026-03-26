from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.const import CONF_OPTIONS as CONF_OPTIONS, CONF_TARGET as CONF_TARGET
from homeassistant.core import HomeAssistant as HomeAssistant, State as State
from homeassistant.helpers.automation import DomainSpec as DomainSpec
from homeassistant.helpers.condition import ATTR_BEHAVIOR as ATTR_BEHAVIOR, BEHAVIOR_ALL as BEHAVIOR_ALL, BEHAVIOR_ANY as BEHAVIOR_ANY, Condition as Condition, ConditionConfig as ConditionConfig, EntityConditionBase as EntityConditionBase

CONF_VALUE: str
_TEXT_CONDITION_SCHEMA: Incomplete

class TextIsEqualToCondition(EntityConditionBase):
    _domain_specs: Incomplete
    _schema = _TEXT_CONDITION_SCHEMA
    _value: str
    def __init__(self, hass: HomeAssistant, config: ConditionConfig) -> None: ...
    def is_valid_state(self, entity_state: State) -> bool: ...

CONDITIONS: dict[str, type[Condition]]

async def async_get_conditions(hass: HomeAssistant) -> dict[str, type[Condition]]: ...

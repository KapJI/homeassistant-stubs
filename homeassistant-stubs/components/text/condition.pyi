from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.const import CONF_OPTIONS as CONF_OPTIONS
from homeassistant.core import HomeAssistant as HomeAssistant, State as State
from homeassistant.helpers.automation import DomainSpec as DomainSpec
from homeassistant.helpers.condition import Condition as Condition, ConditionConfig as ConditionConfig, ENTITY_STATE_CONDITION_SCHEMA_ANY_ALL as ENTITY_STATE_CONDITION_SCHEMA_ANY_ALL, EntityConditionBase as EntityConditionBase

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

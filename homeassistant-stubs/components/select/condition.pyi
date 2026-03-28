from .const import CONF_OPTION as CONF_OPTION, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.const import CONF_OPTIONS as CONF_OPTIONS
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.automation import DomainSpec as DomainSpec
from homeassistant.helpers.condition import Condition as Condition, ConditionConfig as ConditionConfig, ENTITY_STATE_CONDITION_SCHEMA_ANY_ALL as ENTITY_STATE_CONDITION_SCHEMA_ANY_ALL, EntityStateConditionBase as EntityStateConditionBase

IS_OPTION_SELECTED_SCHEMA: Incomplete
SELECT_DOMAIN_SPECS: Incomplete

class IsOptionSelectedCondition(EntityStateConditionBase):
    _domain_specs = SELECT_DOMAIN_SPECS
    _schema = IS_OPTION_SELECTED_SCHEMA
    _states: Incomplete
    def __init__(self, hass: HomeAssistant, config: ConditionConfig) -> None: ...

CONDITIONS: dict[str, type[Condition]]

async def async_get_conditions(hass: HomeAssistant) -> dict[str, type[Condition]]: ...

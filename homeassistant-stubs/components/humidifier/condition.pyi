from .const import ATTR_ACTION as ATTR_ACTION, ATTR_HUMIDITY as ATTR_HUMIDITY, DOMAIN as DOMAIN, HumidifierAction as HumidifierAction, HumidifierEntityFeature as HumidifierEntityFeature
from _typeshed import Incomplete
from homeassistant.const import ATTR_MODE as ATTR_MODE, CONF_OPTIONS as CONF_OPTIONS, PERCENTAGE as PERCENTAGE, STATE_OFF as STATE_OFF, STATE_ON as STATE_ON
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.automation import DomainSpec as DomainSpec
from homeassistant.helpers.condition import Condition as Condition, ConditionConfig as ConditionConfig, ENTITY_STATE_CONDITION_SCHEMA_ANY_ALL as ENTITY_STATE_CONDITION_SCHEMA_ANY_ALL, EntityStateConditionBase as EntityStateConditionBase, make_entity_numerical_condition as make_entity_numerical_condition, make_entity_state_condition as make_entity_state_condition
from homeassistant.helpers.entity import get_supported_features as get_supported_features

CONF_MODE: str
IS_MODE_CONDITION_SCHEMA: Incomplete

def _supports_feature(hass: HomeAssistant, entity_id: str, features: int) -> bool: ...

class IsModeCondition(EntityStateConditionBase):
    _domain_specs: Incomplete
    _schema = IS_MODE_CONDITION_SCHEMA
    _states: Incomplete
    def __init__(self, hass: HomeAssistant, config: ConditionConfig) -> None: ...
    def entity_filter(self, entities: set[str]) -> set[str]: ...

CONDITIONS: dict[str, type[Condition]]

async def async_get_conditions(hass: HomeAssistant) -> dict[str, type[Condition]]: ...

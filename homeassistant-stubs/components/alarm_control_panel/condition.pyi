from .const import AlarmControlPanelEntityFeature as AlarmControlPanelEntityFeature, AlarmControlPanelState as AlarmControlPanelState, DOMAIN as DOMAIN
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.condition import Condition as Condition, EntityStateConditionBase as EntityStateConditionBase, make_entity_state_condition as make_entity_state_condition
from homeassistant.helpers.entity import get_supported_features as get_supported_features

def supports_feature(hass: HomeAssistant, entity_id: str, features: int) -> bool: ...

class EntityStateRequiredFeaturesCondition(EntityStateConditionBase):
    _required_features: int
    def entity_filter(self, entities: set[str]) -> set[str]: ...

def make_entity_state_required_features_condition(domain: str, to_state: str, required_features: int) -> type[EntityStateRequiredFeaturesCondition]: ...

CONDITIONS: dict[str, type[Condition]]

async def async_get_conditions(hass: HomeAssistant) -> dict[str, type[Condition]]: ...

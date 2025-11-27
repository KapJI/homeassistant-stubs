from .const import AlarmControlPanelEntityFeature as AlarmControlPanelEntityFeature, AlarmControlPanelState as AlarmControlPanelState, DOMAIN as DOMAIN
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity import get_supported_features as get_supported_features
from homeassistant.helpers.trigger import EntityStateTriggerBase as EntityStateTriggerBase, Trigger as Trigger, make_conditional_entity_state_trigger as make_conditional_entity_state_trigger, make_entity_state_trigger as make_entity_state_trigger

def supports_feature(hass: HomeAssistant, entity_id: str, features: int) -> bool: ...

class EntityStateTriggerRequiredFeatures(EntityStateTriggerBase):
    _required_features: int
    def entity_filter(self, entities: set[str]) -> set[str]: ...

def make_entity_state_trigger_required_features(domain: str, to_state: str, required_features: int) -> type[EntityStateTriggerBase]: ...

TRIGGERS: dict[str, type[Trigger]]

async def async_get_triggers(hass: HomeAssistant) -> dict[str, type[Trigger]]: ...

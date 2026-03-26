from .const import ATTR_ACTION as ATTR_ACTION, DOMAIN as DOMAIN, HumidifierAction as HumidifierAction, HumidifierEntityFeature as HumidifierEntityFeature
from _typeshed import Incomplete
from homeassistant.const import ATTR_MODE as ATTR_MODE, CONF_OPTIONS as CONF_OPTIONS, STATE_OFF as STATE_OFF, STATE_ON as STATE_ON
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.automation import DomainSpec as DomainSpec
from homeassistant.helpers.entity import get_supported_features as get_supported_features
from homeassistant.helpers.trigger import ENTITY_STATE_TRIGGER_SCHEMA_FIRST_LAST as ENTITY_STATE_TRIGGER_SCHEMA_FIRST_LAST, EntityTargetStateTriggerBase as EntityTargetStateTriggerBase, Trigger as Trigger, TriggerConfig as TriggerConfig, make_entity_target_state_trigger as make_entity_target_state_trigger

CONF_MODE: str
MODE_CHANGED_TRIGGER_SCHEMA: Incomplete

def _supports_feature(hass: HomeAssistant, entity_id: str, features: int) -> bool: ...

class ModeChangedTrigger(EntityTargetStateTriggerBase):
    _domain_specs: Incomplete
    _schema = MODE_CHANGED_TRIGGER_SCHEMA
    _to_states: Incomplete
    def __init__(self, hass: HomeAssistant, config: TriggerConfig) -> None: ...
    def entity_filter(self, entities: set[str]) -> set[str]: ...

TRIGGERS: dict[str, type[Trigger]]

async def async_get_triggers(hass: HomeAssistant) -> dict[str, type[Trigger]]: ...

from .const import ATTR_CURRENT_HUMIDITY as ATTR_CURRENT_HUMIDITY, ATTR_CURRENT_TEMPERATURE as ATTR_CURRENT_TEMPERATURE, ATTR_HUMIDITY as ATTR_HUMIDITY, ATTR_HVAC_ACTION as ATTR_HVAC_ACTION, DOMAIN as DOMAIN, HVACAction as HVACAction, HVACMode as HVACMode
from _typeshed import Incomplete
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, CONF_OPTIONS as CONF_OPTIONS
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.trigger import ENTITY_STATE_TRIGGER_SCHEMA_FIRST_LAST as ENTITY_STATE_TRIGGER_SCHEMA_FIRST_LAST, EntityTargetStateTriggerBase as EntityTargetStateTriggerBase, Trigger as Trigger, TriggerConfig as TriggerConfig, make_entity_numerical_state_attribute_changed_trigger as make_entity_numerical_state_attribute_changed_trigger, make_entity_numerical_state_attribute_crossed_threshold_trigger as make_entity_numerical_state_attribute_crossed_threshold_trigger, make_entity_target_state_attribute_trigger as make_entity_target_state_attribute_trigger, make_entity_target_state_trigger as make_entity_target_state_trigger, make_entity_transition_trigger as make_entity_transition_trigger

CONF_HVAC_MODE: str
HVAC_MODE_CHANGED_TRIGGER_SCHEMA: Incomplete

class HVACModeChangedTrigger(EntityTargetStateTriggerBase):
    _domain = DOMAIN
    _schema = HVAC_MODE_CHANGED_TRIGGER_SCHEMA
    _to_states: Incomplete
    def __init__(self, hass: HomeAssistant, config: TriggerConfig) -> None: ...

TRIGGERS: dict[str, type[Trigger]]

async def async_get_triggers(hass: HomeAssistant) -> dict[str, type[Trigger]]: ...

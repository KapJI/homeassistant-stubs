from .const import DOMAIN as DOMAIN
from homeassistant.const import STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN
from homeassistant.core import HomeAssistant as HomeAssistant, State as State
from homeassistant.helpers.trigger import ENTITY_STATE_TRIGGER_SCHEMA as ENTITY_STATE_TRIGGER_SCHEMA, EntityTriggerBase as EntityTriggerBase, Trigger as Trigger

class TextChangedTrigger(EntityTriggerBase):
    _domain = DOMAIN
    _schema = ENTITY_STATE_TRIGGER_SCHEMA
    def is_valid_state(self, state: State) -> bool: ...

TRIGGERS: dict[str, type[Trigger]]

async def async_get_triggers(hass: HomeAssistant) -> dict[str, type[Trigger]]: ...

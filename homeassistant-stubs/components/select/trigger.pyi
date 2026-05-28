from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.automation import DomainSpec as DomainSpec
from homeassistant.helpers.trigger import ENTITY_STATE_TRIGGER_SCHEMA as ENTITY_STATE_TRIGGER_SCHEMA, EntityTriggerBase as EntityTriggerBase, Trigger as Trigger

class SelectionChangedTrigger(EntityTriggerBase):
    _domain_specs: Incomplete
    _schema = ENTITY_STATE_TRIGGER_SCHEMA

TRIGGERS: dict[str, type[Trigger]]

async def async_get_triggers(hass: HomeAssistant) -> dict[str, type[Trigger]]: ...

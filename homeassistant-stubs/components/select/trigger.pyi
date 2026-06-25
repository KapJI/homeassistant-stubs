from .const import DOMAIN as DOMAIN
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.automation import DomainSpec as DomainSpec
from homeassistant.helpers.trigger import ENTITY_STATE_TRIGGER_SCHEMA as ENTITY_STATE_TRIGGER_SCHEMA, EntityTriggerBase as EntityTriggerBase, Trigger as Trigger

SELECT_DOMAIN_SPECS: dict[str, DomainSpec]

class SelectionChangedTrigger(EntityTriggerBase):
    _domain_specs = SELECT_DOMAIN_SPECS
    _schema = ENTITY_STATE_TRIGGER_SCHEMA

TRIGGERS: dict[str, type[Trigger]]

async def async_get_triggers(hass: HomeAssistant) -> dict[str, type[Trigger]]: ...

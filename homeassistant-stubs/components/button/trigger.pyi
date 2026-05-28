from . import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.automation import DomainSpec as DomainSpec
from homeassistant.helpers.trigger import StatelessEntityTriggerBase as StatelessEntityTriggerBase, Trigger as Trigger

class ButtonPressedTrigger(StatelessEntityTriggerBase):
    _domain_specs: Incomplete

TRIGGERS: dict[str, type[Trigger]]

async def async_get_triggers(hass: HomeAssistant) -> dict[str, type[Trigger]]: ...

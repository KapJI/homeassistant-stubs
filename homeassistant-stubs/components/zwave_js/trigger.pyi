from .triggers import event as event, value_updated as value_updated
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.trigger import Trigger as Trigger

TRIGGERS: Incomplete

async def async_get_triggers(hass: HomeAssistant) -> dict[str, type[Trigger]]: ...

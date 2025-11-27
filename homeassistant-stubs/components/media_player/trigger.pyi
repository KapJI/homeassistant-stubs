from . import MediaPlayerState as MediaPlayerState
from .const import DOMAIN as DOMAIN
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.trigger import Trigger as Trigger, make_conditional_entity_state_trigger as make_conditional_entity_state_trigger

TRIGGERS: dict[str, type[Trigger]]

async def async_get_triggers(hass: HomeAssistant) -> dict[str, type[Trigger]]: ...

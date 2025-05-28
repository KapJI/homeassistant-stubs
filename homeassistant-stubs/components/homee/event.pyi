from . import HomeeConfigEntry as HomeeConfigEntry
from .entity import HomeeEntity as HomeeEntity
from _typeshed import Incomplete
from homeassistant.components.event import EventDeviceClass as EventDeviceClass, EventEntity as EventEntity
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pyHomee.model import HomeeAttribute as HomeeAttribute

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, config_entry: HomeeConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class HomeeEvent(HomeeEntity, EventEntity):
    _attr_translation_key: str
    _attr_event_types: Incomplete
    _attr_device_class: Incomplete
    async def async_added_to_hass(self) -> None: ...
    @callback
    def _event_triggered(self, event: HomeeAttribute) -> None: ...

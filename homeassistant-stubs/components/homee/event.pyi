from . import HomeeConfigEntry as HomeeConfigEntry
from .entity import HomeeEntity as HomeeEntity
from .helpers import setup_homee_platform as setup_homee_platform
from _typeshed import Incomplete
from homeassistant.components.event import EventDeviceClass as EventDeviceClass, EventEntity as EventEntity, EventEntityDescription as EventEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pyHomee.const import AttributeType
from pyHomee.model import HomeeAttribute as HomeeAttribute, HomeeNode as HomeeNode

PARALLEL_UPDATES: int
REMOTE_PROFILES: Incomplete
EVENT_DESCRIPTIONS: dict[AttributeType, EventEntityDescription]

async def add_event_entities(config_entry: HomeeConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback, nodes: list[HomeeNode]) -> None: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: HomeeConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class HomeeEvent(HomeeEntity, EventEntity):
    entity_description: Incomplete
    _attr_translation_key: Incomplete
    _attr_translation_placeholders: Incomplete
    def __init__(self, attribute: HomeeAttribute, entry: HomeeConfigEntry, description: EventEntityDescription) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @callback
    def _event_triggered(self, event: HomeeAttribute) -> None: ...

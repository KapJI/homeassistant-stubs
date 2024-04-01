from ..entity import AxisEventDescription as AxisEventDescription, AxisEventEntity as AxisEventEntity
from .hub import AxisHub as AxisHub
from _typeshed import Incomplete
from axis.models.event import Event as Event
from homeassistant.core import callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

class AxisEntityLoader:
    hub: Incomplete
    registered_events: Incomplete
    topic_to_entity: Incomplete
    def __init__(self, hub: AxisHub) -> None: ...
    def register_platform(self, async_add_entities: AddEntitiesCallback, entity_class: type[AxisEventEntity], descriptions: tuple[AxisEventDescription, ...]) -> None: ...
    def _create_entities_from_event(self, event: Event) -> None: ...
    def initialize_platforms(self) -> None: ...

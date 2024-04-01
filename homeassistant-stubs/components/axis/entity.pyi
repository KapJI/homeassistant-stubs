import abc
from .hub import AxisHub as AxisHub
from _typeshed import Incomplete
from abc import abstractmethod
from axis.models.event import Event as Event, EventTopic
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.core import callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity import Entity as Entity, EntityDescription as EntityDescription

TOPIC_TO_EVENT_TYPE: Incomplete

@dataclass(frozen=True, kw_only=True)
class AxisEventDescription(EntityDescription):
    event_topic: tuple[EventTopic, ...] | EventTopic
    name_fn: Callable[[AxisHub, Event], str] = ...
    supported_fn: Callable[[AxisHub, Event], bool] = ...
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, event_topic, name_fn, supported_fn) -> None: ...

class AxisEntity(Entity):
    _attr_has_entity_name: bool
    hub: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, hub: AxisHub) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    _attr_available: Incomplete
    def async_signal_reachable_callback(self) -> None: ...

class AxisEventEntity(AxisEntity, metaclass=abc.ABCMeta):
    entity_description: AxisEventDescription
    _attr_should_poll: bool
    _event_id: Incomplete
    _event_topic: Incomplete
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, hub: AxisHub, description: AxisEventDescription, event: Event) -> None: ...
    @abstractmethod
    def async_event_callback(self, event: Event) -> None: ...
    async def async_added_to_hass(self) -> None: ...

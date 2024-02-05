import abc
from .device import AxisNetworkDevice as AxisNetworkDevice
from _typeshed import Incomplete
from abc import abstractmethod
from axis.models.event import Event as Event
from homeassistant.core import callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity import Entity as Entity

TOPIC_TO_EVENT_TYPE: Incomplete

class AxisEntity(Entity):
    _attr_has_entity_name: bool
    device: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, device: AxisNetworkDevice) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    _attr_available: Incomplete
    def async_signal_reachable_callback(self) -> None: ...

class AxisEventEntity(AxisEntity, metaclass=abc.ABCMeta):
    _attr_should_poll: bool
    _event_id: Incomplete
    _event_topic: Incomplete
    _event_type: Incomplete
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_class: Incomplete
    def __init__(self, event: Event, device: AxisNetworkDevice) -> None: ...
    @abstractmethod
    def async_event_callback(self, event: Event) -> None: ...
    async def async_added_to_hass(self) -> None: ...

import abc
import aiounifi
from .const import ATTR_MANUFACTURER as ATTR_MANUFACTURER
from .controller import UniFiController as UniFiController
from _typeshed import Incomplete
from abc import abstractmethod
from aiounifi.interfaces.api_handlers import APIHandler, CallbackType, ItemEvent, UnsubscribeType
from aiounifi.models.api import ApiItemT
from aiounifi.models.event import Event as Event, EventKey as EventKey
from collections.abc import Callable
from homeassistant.core import callback as callback
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo, Entity as Entity, EntityDescription as EntityDescription
from typing import Generic, TypeVar

HandlerT = TypeVar('HandlerT', bound=APIHandler)
SubscriptionT = Callable[[CallbackType, ItemEvent], UnsubscribeType]

def async_device_available_fn(controller: UniFiController, obj_id: str) -> bool: ...
def async_device_device_info_fn(api: aiounifi.Controller, obj_id: str) -> DeviceInfo: ...

class UnifiDescription(Generic[HandlerT, ApiItemT]):
    allowed_fn: Callable[[UniFiController, str], bool]
    api_handler_fn: Callable[[aiounifi.Controller], HandlerT]
    available_fn: Callable[[UniFiController, str], bool]
    device_info_fn: Callable[[aiounifi.Controller, str], DeviceInfo | None]
    event_is_on: tuple[EventKey, ...] | None
    event_to_subscribe: tuple[EventKey, ...] | None
    name_fn: Callable[[ApiItemT], str | None]
    object_fn: Callable[[aiounifi.Controller, str], ApiItemT]
    supported_fn: Callable[[UniFiController, str], bool | None]
    unique_id_fn: Callable[[UniFiController, str], str]
    def __init__(self, allowed_fn, api_handler_fn, available_fn, device_info_fn, event_is_on, event_to_subscribe, name_fn, object_fn, supported_fn, unique_id_fn) -> None: ...

class UnifiEntityDescription(EntityDescription, UnifiDescription[HandlerT, ApiItemT]):
    def __init__(self, allowed_fn, api_handler_fn, available_fn, device_info_fn, event_is_on, event_to_subscribe, name_fn, object_fn, supported_fn, unique_id_fn, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement) -> None: ...

class UnifiEntity(Entity, Generic[HandlerT, ApiItemT], metaclass=abc.ABCMeta):
    entity_description: UnifiEntityDescription[HandlerT, ApiItemT]
    _attr_should_poll: bool
    _attr_unique_id: str
    _obj_id: Incomplete
    controller: Incomplete
    _removed: bool
    _attr_available: Incomplete
    _attr_device_info: Incomplete
    _attr_name: Incomplete
    def __init__(self, obj_id: str, controller: UniFiController, description: UnifiEntityDescription[HandlerT, ApiItemT]) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    def async_signalling_callback(self, event: ItemEvent, obj_id: str) -> None: ...
    def async_signal_reachable_callback(self) -> None: ...
    async def async_signal_options_updated(self) -> None: ...
    async def remove_item(self, keys: set) -> None: ...
    def async_initiate_state(self) -> None: ...
    @abstractmethod
    def async_update_state(self, event: ItemEvent, obj_id: str) -> None: ...
    def async_event_callback(self, event: Event) -> None: ...

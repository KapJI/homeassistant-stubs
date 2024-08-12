import abc
import aiounifi
from .const import ATTR_MANUFACTURER as ATTR_MANUFACTURER, DOMAIN as DOMAIN
from .hub import UnifiHub as UnifiHub
from _typeshed import Incomplete
from abc import abstractmethod
from aiounifi.interfaces.api_handlers import APIHandler, CallbackType, ItemEvent, UnsubscribeType
from aiounifi.models.api import ApiItemT as ApiItemT
from aiounifi.models.event import Event as Event, EventKey as EventKey
from collections.abc import Callable
from dataclasses import dataclass
from homeassistant.core import callback as callback
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC, DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity import Entity as Entity, EntityDescription as EntityDescription
from typing import Generic, TypeVar

HandlerT = TypeVar('HandlerT', bound=APIHandler)
SubscriptionT = Callable[[CallbackType, ItemEvent], UnsubscribeType]

def async_device_available_fn(hub: UnifiHub, obj_id: str) -> bool: ...
def async_wlan_available_fn(hub: UnifiHub, obj_id: str) -> bool: ...
def async_device_device_info_fn(hub: UnifiHub, obj_id: str) -> DeviceInfo: ...
def async_wlan_device_info_fn(hub: UnifiHub, obj_id: str) -> DeviceInfo: ...
def async_client_device_info_fn(hub: UnifiHub, obj_id: str) -> DeviceInfo: ...

@dataclass(frozen=True, kw_only=True)
class UnifiEntityDescription(EntityDescription, Generic[HandlerT, ApiItemT]):
    api_handler_fn: Callable[[aiounifi.Controller], HandlerT]
    device_info_fn: Callable[[UnifiHub, str], DeviceInfo | None]
    object_fn: Callable[[aiounifi.Controller, str], ApiItemT]
    unique_id_fn: Callable[[UnifiHub, str], str]
    allowed_fn: Callable[[UnifiHub, str], bool] = ...
    available_fn: Callable[[UnifiHub, str], bool] = ...
    name_fn: Callable[[ApiItemT], str | None] = ...
    supported_fn: Callable[[UnifiHub, str], bool] = ...
    has_entity_name = ...
    event_is_on: set[EventKey] | None = ...
    event_to_subscribe: tuple[EventKey, ...] | None = ...
    should_poll: bool = ...
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=..., api_handler_fn, device_info_fn, object_fn, unique_id_fn, allowed_fn=..., available_fn=..., name_fn=..., supported_fn=..., event_is_on=..., event_to_subscribe=..., should_poll=...) -> None: ...

class UnifiEntity(Entity, Generic[HandlerT, ApiItemT], metaclass=abc.ABCMeta):
    entity_description: UnifiEntityDescription[HandlerT, ApiItemT]
    _attr_unique_id: str
    _obj_id: Incomplete
    hub: Incomplete
    api: Incomplete
    _removed: bool
    _attr_available: Incomplete
    _attr_device_info: Incomplete
    _attr_should_poll: Incomplete
    _attr_name: Incomplete
    def __init__(self, obj_id: str, hub: UnifiHub, description: UnifiEntityDescription[HandlerT, ApiItemT]) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    def async_signalling_callback(self, event: ItemEvent, obj_id: str) -> None: ...
    def async_signal_reachable_callback(self) -> None: ...
    async def async_signal_options_updated(self) -> None: ...
    async def remove_item(self, keys: set) -> None: ...
    async def async_update(self) -> None: ...
    def async_initiate_state(self) -> None: ...
    @abstractmethod
    def async_update_state(self, event: ItemEvent, obj_id: str) -> None: ...
    def async_event_callback(self, event: Event) -> None: ...

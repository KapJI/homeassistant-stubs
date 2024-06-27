from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from deebot_client.capabilities import Capabilities as Capabilities
from deebot_client.device import Device as Device
from deebot_client.events.base import Event
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import Entity as Entity, EntityDescription as EntityDescription
from typing import Any, Generic, TypeVar

CapabilityEntity = TypeVar('CapabilityEntity')
EventT = TypeVar('EventT', bound=Event)

class EcovacsEntity(Entity, Generic[CapabilityEntity]):
    _attr_should_poll: bool
    _attr_has_entity_name: bool
    _always_available: bool
    _attr_unique_id: Incomplete
    _device: Incomplete
    _capability: Incomplete
    _subscribed_events: Incomplete
    def __init__(self, device: Device, capability: CapabilityEntity, **kwargs: Any) -> None: ...
    @property
    def device_info(self) -> DeviceInfo | None: ...
    _attr_available: Incomplete
    async def async_added_to_hass(self) -> None: ...
    def _subscribe(self, event_type: type[EventT], callback: Callable[[EventT], Coroutine[Any, Any, None]]) -> None: ...
    async def async_update(self) -> None: ...

class EcovacsDescriptionEntity(EcovacsEntity[CapabilityEntity]):
    entity_description: Incomplete
    def __init__(self, device: Device, capability: CapabilityEntity, entity_description: EntityDescription, **kwargs: Any) -> None: ...

@dataclass(kw_only=True, frozen=True)
class EcovacsCapabilityEntityDescription(EntityDescription, Generic[CapabilityEntity]):
    capability_fn: Callable[[Capabilities], CapabilityEntity | None]
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, capability_fn) -> None: ...

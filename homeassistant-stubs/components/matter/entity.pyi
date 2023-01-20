import abc
from .const import DOMAIN as DOMAIN, ID_TYPE_DEVICE_ID as ID_TYPE_DEVICE_ID
from .helpers import get_device_id as get_device_id, get_operational_instance_id as get_operational_instance_id
from _typeshed import Incomplete
from abc import abstractmethod
from collections.abc import Callable as Callable
from homeassistant.core import callback as callback
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo, Entity as Entity, EntityDescription as EntityDescription
from matter_server.client import MatterClient as MatterClient
from matter_server.common.models.device_type_instance import MatterDeviceTypeInstance as MatterDeviceTypeInstance
from matter_server.common.models.events import EventType
from matter_server.common.models.node import MatterAttribute as MatterAttribute
from matter_server.common.models.node_device import AbstractMatterNodeDevice as AbstractMatterNodeDevice
from typing import Any

LOGGER: Incomplete

class MatterEntityDescription:
    entity_cls: type[MatterEntity]
    subscribe_attributes: tuple
    def __init__(self, entity_cls, subscribe_attributes) -> None: ...

class MatterEntityDescriptionBaseClass(EntityDescription, MatterEntityDescription):
    def __init__(self, entity_cls, subscribe_attributes, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement) -> None: ...

class MatterEntity(Entity, metaclass=abc.ABCMeta):
    entity_description: MatterEntityDescriptionBaseClass
    _attr_should_poll: bool
    _attr_has_entity_name: bool
    matter_client: Incomplete
    _node_device: Incomplete
    _device_type_instance: Incomplete
    _unsubscribes: Incomplete
    _attributes_map: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, matter_client: MatterClient, node_device: AbstractMatterNodeDevice, device_type_instance: MatterDeviceTypeInstance, entity_description: MatterEntityDescriptionBaseClass) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    def _on_matter_event(self, event: EventType, data: Any = ...) -> None: ...
    @abstractmethod
    def _update_from_device(self) -> None: ...
    def get_matter_attribute(self, attribute: type) -> Union[MatterAttribute, None]: ...

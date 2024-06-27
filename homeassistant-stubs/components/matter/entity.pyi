import abc
from .const import DOMAIN as DOMAIN, ID_TYPE_DEVICE_ID as ID_TYPE_DEVICE_ID
from .discovery import MatterEntityInfo as MatterEntityInfo
from .helpers import get_device_id as get_device_id
from _typeshed import Incomplete
from abc import abstractmethod
from chip.clusters.Objects import ClusterAttributeDescriptor as ClusterAttributeDescriptor
from collections.abc import Callable as Callable
from dataclasses import dataclass
from functools import cached_property as cached_property
from homeassistant.core import callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import Entity as Entity, EntityDescription as EntityDescription
from homeassistant.helpers.typing import UndefinedType as UndefinedType
from matter_server.client import MatterClient as MatterClient
from matter_server.client.models.node import MatterEndpoint as MatterEndpoint
from matter_server.common.models import EventType
from typing import Any

LOGGER: Incomplete

@dataclass(frozen=True)
class MatterEntityDescription(EntityDescription):
    measurement_to_ha: Callable[[Any], Any] | None = ...
    ha_to_native_value: Callable[[Any], Any] | None = ...
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, measurement_to_ha, ha_to_native_value) -> None: ...

class MatterEntity(Entity, metaclass=abc.ABCMeta):
    _attr_has_entity_name: bool
    _name_postfix: str | None
    matter_client: Incomplete
    _endpoint: Incomplete
    _entity_info: Incomplete
    entity_description: Incomplete
    _unsubscribes: Incomplete
    _attributes_map: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    _attr_available: Incomplete
    _attr_name: Incomplete
    def __init__(self, matter_client: MatterClient, endpoint: MatterEndpoint, entity_info: MatterEntityInfo) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @cached_property
    def name(self) -> str | UndefinedType | None: ...
    def _on_matter_event(self, event: EventType, data: Any = None) -> None: ...
    @abstractmethod
    def _update_from_device(self) -> None: ...
    def get_matter_attribute_value(self, attribute: type[ClusterAttributeDescriptor], null_as_none: bool = True) -> Any: ...
    def get_matter_attribute_path(self, attribute: type[ClusterAttributeDescriptor]) -> str: ...

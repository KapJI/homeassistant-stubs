from _typeshed import Incomplete
from chip.clusters.Objects import ClusterAttributeDescriptor as ClusterAttributeDescriptor
from collections.abc import Callable as Callable
from homeassistant.const import Platform as Platform
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from matter_server.client.models.device_types import DeviceType as DeviceType
from matter_server.client.models.node import MatterEndpoint as MatterEndpoint
from typing import Any

class DataclassMustHaveAtLeastOne:
    def __post_init__(self) -> None: ...

SensorValueTypes: Incomplete

class MatterEntityInfo:
    endpoint: MatterEndpoint
    platform: Platform
    attributes_to_watch: list[type[ClusterAttributeDescriptor]]
    entity_description: EntityDescription
    entity_class: type
    measurement_to_ha: Union[Callable[[SensorValueTypes], SensorValueTypes], None]
    @property
    def primary_attribute(self) -> type[ClusterAttributeDescriptor]: ...
    def __init__(self, endpoint, platform, attributes_to_watch, entity_description, entity_class, measurement_to_ha) -> None: ...

class MatterDiscoverySchema:
    platform: Platform
    entity_description: EntityDescription
    entity_class: type
    required_attributes: tuple[type[ClusterAttributeDescriptor], ...]
    device_type: Union[tuple[Union[type[DeviceType], DeviceType], ...], None]
    not_device_type: Union[tuple[Union[type[DeviceType], DeviceType], ...], None]
    vendor_id: Union[tuple[int, ...], None]
    product_name: Union[tuple[str, ...], None]
    endpoint_id: Union[tuple[int, ...], None]
    absent_attributes: Union[tuple[type[ClusterAttributeDescriptor], ...], None]
    optional_attributes: Union[tuple[type[ClusterAttributeDescriptor], ...], None]
    allow_multi: bool
    measurement_to_ha: Union[Callable[[Any], Any], None]
    def __init__(self, platform, entity_description, entity_class, required_attributes, device_type, not_device_type, vendor_id, product_name, endpoint_id, absent_attributes, optional_attributes, allow_multi, measurement_to_ha) -> None: ...

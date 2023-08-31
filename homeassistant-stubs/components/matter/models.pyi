from _typeshed import Incomplete
from chip.clusters.Objects import ClusterAttributeDescriptor as ClusterAttributeDescriptor
from homeassistant.const import Platform as Platform
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from matter_server.client.models.device_types import DeviceType as DeviceType
from matter_server.client.models.node import MatterEndpoint as MatterEndpoint

SensorValueTypes: Incomplete

class MatterEntityInfo:
    endpoint: MatterEndpoint
    platform: Platform
    attributes_to_watch: list[type[ClusterAttributeDescriptor]]
    entity_description: EntityDescription
    entity_class: type
    @property
    def primary_attribute(self) -> type[ClusterAttributeDescriptor]: ...
    def __init__(self, endpoint, platform, attributes_to_watch, entity_description, entity_class) -> None: ...

class MatterDiscoverySchema:
    platform: Platform
    entity_description: EntityDescription
    entity_class: type
    required_attributes: tuple[type[ClusterAttributeDescriptor], ...]
    device_type: tuple[type[DeviceType] | DeviceType, ...] | None
    not_device_type: tuple[type[DeviceType] | DeviceType, ...] | None
    vendor_id: tuple[int, ...] | None
    product_name: tuple[str, ...] | None
    endpoint_id: tuple[int, ...] | None
    absent_attributes: tuple[type[ClusterAttributeDescriptor], ...] | None
    optional_attributes: tuple[type[ClusterAttributeDescriptor], ...] | None
    allow_multi: bool
    def __init__(self, platform, entity_description, entity_class, required_attributes, device_type, not_device_type, vendor_id, product_name, endpoint_id, absent_attributes, optional_attributes, allow_multi) -> None: ...

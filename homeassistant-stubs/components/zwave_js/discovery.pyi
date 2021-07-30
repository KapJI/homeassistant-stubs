from .discovery_data_template import BaseDiscoverySchemaDataTemplate as BaseDiscoverySchemaDataTemplate, DynamicCurrentTempClimateDataTemplate as DynamicCurrentTempClimateDataTemplate, ZwaveValueID as ZwaveValueID
from awesomeversion import AwesomeVersion
from collections.abc import Generator
from homeassistant.core import callback as callback
from typing import Any
from zwave_js_server.model.device_class import DeviceClassItem as DeviceClassItem
from zwave_js_server.model.node import Node as ZwaveNode
from zwave_js_server.model.value import Value as ZwaveValue

class DataclassMustHaveAtLeastOne:
    def __post_init__(self) -> None: ...

class FirmwareVersionRange(DataclassMustHaveAtLeastOne):
    min: Union[str, None]
    max: Union[str, None]
    min_ver: Union[AwesomeVersion, None]
    max_ver: Union[AwesomeVersion, None]
    def __post_init__(self) -> None: ...

class ZwaveDiscoveryInfo:
    node: ZwaveNode
    primary_value: ZwaveValue
    assumed_state: bool
    platform: str
    platform_hint: Union[str, None]
    platform_data_template: Union[BaseDiscoverySchemaDataTemplate, None]
    platform_data: Union[dict[str, Any], None]
    additional_value_ids_to_watch: Union[set[str], None]
    entity_registry_enabled_default: bool

class ZWaveValueDiscoverySchema(DataclassMustHaveAtLeastOne):
    command_class: Union[set[int], None]
    endpoint: Union[set[int], None]
    property: Union[set[Union[str, int]], None]
    property_name: Union[set[str], None]
    property_key: Union[set[Union[str, int]], None]
    property_key_name: Union[set[str], None]
    type: Union[set[str], None]

class ZWaveDiscoverySchema:
    platform: str
    primary_value: ZWaveValueDiscoverySchema
    hint: Union[str, None]
    data_template: Union[BaseDiscoverySchemaDataTemplate, None]
    manufacturer_id: Union[set[int], None]
    product_id: Union[set[int], None]
    product_type: Union[set[int], None]
    firmware_version_range: Union[FirmwareVersionRange, None]
    firmware_version: Union[set[str], None]
    device_class_basic: Union[set[Union[str, int]], None]
    device_class_generic: Union[set[Union[str, int]], None]
    device_class_specific: Union[set[Union[str, int]], None]
    required_values: Union[list[ZWaveValueDiscoverySchema], None]
    absent_values: Union[list[ZWaveValueDiscoverySchema], None]
    allow_multi: bool
    assumed_state: bool
    entity_registry_enabled_default: bool

def get_config_parameter_discovery_schema(property_: Union[set[Union[str, int]], None] = ..., property_name: Union[set[str], None] = ..., property_key: Union[set[Union[str, int]], None] = ..., property_key_name: Union[set[str], None] = ..., **kwargs: Any) -> ZWaveDiscoverySchema: ...

SWITCH_MULTILEVEL_CURRENT_VALUE_SCHEMA: Any
SWITCH_BINARY_CURRENT_VALUE_SCHEMA: Any
SIREN_TONE_SCHEMA: Any
DISCOVERY_SCHEMAS: Any

def async_discover_values(node: ZwaveNode) -> Generator[ZwaveDiscoveryInfo, None, None]: ...
def check_value(value: ZwaveValue, schema: ZWaveValueDiscoverySchema) -> bool: ...
def check_device_class(device_class: DeviceClassItem, required_value: Union[set[Union[str, int]], None]) -> bool: ...

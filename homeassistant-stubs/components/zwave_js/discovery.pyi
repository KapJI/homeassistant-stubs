from .const import LOGGER as LOGGER
from .discovery_data_template import BaseDiscoverySchemaDataTemplate as BaseDiscoverySchemaDataTemplate, ConfigurableFanValueMappingDataTemplate as ConfigurableFanValueMappingDataTemplate, CoverTiltDataTemplate as CoverTiltDataTemplate, DynamicCurrentTempClimateDataTemplate as DynamicCurrentTempClimateDataTemplate, FanValueMapping as FanValueMapping, FixedFanValueMappingDataTemplate as FixedFanValueMappingDataTemplate, NumericSensorDataTemplate as NumericSensorDataTemplate
from .helpers import ZwaveValueID as ZwaveValueID
from _typeshed import Incomplete
from awesomeversion import AwesomeVersion
from collections.abc import Generator
from homeassistant.backports.enum import StrEnum as StrEnum
from homeassistant.const import Platform as Platform
from homeassistant.core import callback as callback
from homeassistant.helpers.device_registry import DeviceEntry as DeviceEntry
from typing import Any
from zwave_js_server.model.device_class import DeviceClassItem as DeviceClassItem
from zwave_js_server.model.node import Node as ZwaveNode
from zwave_js_server.model.value import Value as ZwaveValue

class ValueType(StrEnum):
    ANY: str
    BOOLEAN: str
    NUMBER: str
    STRING: str

class DataclassMustHaveAtLeastOne:
    def __post_init__(self) -> None: ...

class FirmwareVersionRange(DataclassMustHaveAtLeastOne):
    min: Union[str, None]
    max: Union[str, None]
    min_ver: Union[AwesomeVersion, None]
    max_ver: Union[AwesomeVersion, None]
    def __post_init__(self) -> None: ...
    def __init__(self, min, max) -> None: ...

class ZwaveDiscoveryInfo:
    node: ZwaveNode
    primary_value: ZwaveValue
    assumed_state: bool
    platform: Platform
    platform_data: Any
    additional_value_ids_to_watch: set[str]
    platform_hint: Union[str, None]
    platform_data_template: Union[BaseDiscoverySchemaDataTemplate, None]
    entity_registry_enabled_default: bool
    def __init__(self, node, primary_value, assumed_state, platform, platform_data, additional_value_ids_to_watch, platform_hint, platform_data_template, entity_registry_enabled_default) -> None: ...

class ZWaveValueDiscoverySchema(DataclassMustHaveAtLeastOne):
    command_class: Union[set[int], None]
    endpoint: Union[set[int], None]
    property: Union[set[Union[str, int]], None]
    property_name: Union[set[str], None]
    property_key: Union[set[Union[str, int, None]], None]
    property_key_name: Union[set[Union[str, None]], None]
    type: Union[set[str], None]
    def __init__(self, command_class, endpoint, property, property_name, property_key, property_key_name, type) -> None: ...

class ZWaveDiscoverySchema:
    platform: Platform
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
    def __init__(self, platform, primary_value, hint, data_template, manufacturer_id, product_id, product_type, firmware_version_range, firmware_version, device_class_basic, device_class_generic, device_class_specific, required_values, absent_values, allow_multi, assumed_state, entity_registry_enabled_default) -> None: ...

def get_config_parameter_discovery_schema(property_: Union[set[Union[str, int]], None] = ..., property_name: Union[set[str], None] = ..., property_key: Union[set[Union[str, int, None]], None] = ..., property_key_name: Union[set[Union[str, None]], None] = ..., **kwargs: Any) -> ZWaveDiscoverySchema: ...

DOOR_LOCK_CURRENT_MODE_SCHEMA: Incomplete
SWITCH_MULTILEVEL_CURRENT_VALUE_SCHEMA: Incomplete
SWITCH_BINARY_CURRENT_VALUE_SCHEMA: Incomplete
SIREN_TONE_SCHEMA: Incomplete
DISCOVERY_SCHEMAS: Incomplete

def async_discover_node_values(node: ZwaveNode, device: DeviceEntry, discovered_value_ids: dict[str, set[str]]) -> Generator[ZwaveDiscoveryInfo, None, None]: ...
def async_discover_single_value(value: ZwaveValue, device: DeviceEntry, discovered_value_ids: dict[str, set[str]]) -> Generator[ZwaveDiscoveryInfo, None, None]: ...
def check_value(value: ZwaveValue, schema: ZWaveValueDiscoverySchema) -> bool: ...
def check_device_class(device_class: DeviceClassItem, required_value: Union[set[Union[str, int]], None]) -> bool: ...

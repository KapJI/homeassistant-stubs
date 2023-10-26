from .const import COVER_POSITION_PROPERTY_KEYS as COVER_POSITION_PROPERTY_KEYS, COVER_TILT_PROPERTY_KEYS as COVER_TILT_PROPERTY_KEYS, LOGGER as LOGGER
from .discovery_data_template import BaseDiscoverySchemaDataTemplate as BaseDiscoverySchemaDataTemplate, ConfigurableFanValueMappingDataTemplate as ConfigurableFanValueMappingDataTemplate, CoverTiltDataTemplate as CoverTiltDataTemplate, DynamicCurrentTempClimateDataTemplate as DynamicCurrentTempClimateDataTemplate, FanValueMapping as FanValueMapping, FixedFanValueMappingDataTemplate as FixedFanValueMappingDataTemplate, NumericSensorDataTemplate as NumericSensorDataTemplate
from .helpers import ZwaveValueID as ZwaveValueID
from _typeshed import Incomplete
from awesomeversion import AwesomeVersion
from collections.abc import Generator
from enum import StrEnum
from homeassistant.const import EntityCategory as EntityCategory, Platform as Platform
from homeassistant.core import callback as callback
from homeassistant.helpers.device_registry import DeviceEntry as DeviceEntry
from typing import Any
from zwave_js_server.model.device_class import DeviceClassItem as DeviceClassItem
from zwave_js_server.model.node import Node as ZwaveNode
from zwave_js_server.model.value import ConfigurationValue, Value as ZwaveValue

class ValueType(StrEnum):
    ANY: str
    BOOLEAN: str
    NUMBER: str
    STRING: str

class DataclassMustHaveAtLeastOne:
    def __post_init__(self) -> None: ...

class FirmwareVersionRange(DataclassMustHaveAtLeastOne):
    min: str | None
    max: str | None
    min_ver: AwesomeVersion | None
    max_ver: AwesomeVersion | None
    def __post_init__(self) -> None: ...
    def __init__(self, min, max) -> None: ...

class ZwaveDiscoveryInfo:
    node: ZwaveNode
    primary_value: ZwaveValue
    assumed_state: bool
    platform: Platform
    platform_data: Any
    additional_value_ids_to_watch: set[str]
    platform_hint: str | None
    platform_data_template: BaseDiscoverySchemaDataTemplate | None
    entity_registry_enabled_default: bool
    entity_category: EntityCategory | None
    def __init__(self, node, primary_value, assumed_state, platform, platform_data, additional_value_ids_to_watch, platform_hint, platform_data_template, entity_registry_enabled_default, entity_category) -> None: ...

class ZWaveValueDiscoverySchema(DataclassMustHaveAtLeastOne):
    command_class: set[int] | None
    endpoint: set[int] | None
    property: set[str | int] | None
    property_name: set[str] | None
    property_key: set[str | int | None] | None
    not_property_key: set[str | int | None] | None
    type: set[str] | None
    readable: bool | None
    writeable: bool | None
    any_available_states: set[tuple[int, str]] | None
    value: Any | None
    stateful: bool | None
    def __init__(self, command_class, endpoint, property, property_name, property_key, not_property_key, type, readable, writeable, any_available_states, value, stateful) -> None: ...

class ZWaveDiscoverySchema:
    platform: Platform
    primary_value: ZWaveValueDiscoverySchema
    hint: str | None
    data_template: BaseDiscoverySchemaDataTemplate | None
    manufacturer_id: set[int] | None
    product_id: set[int] | None
    product_type: set[int] | None
    firmware_version_range: FirmwareVersionRange | None
    device_class_generic: set[str] | None
    device_class_specific: set[str] | None
    required_values: list[ZWaveValueDiscoverySchema] | None
    absent_values: list[ZWaveValueDiscoverySchema] | None
    allow_multi: bool
    assumed_state: bool
    entity_registry_enabled_default: bool
    entity_category: EntityCategory | None
    def __init__(self, platform, primary_value, hint, data_template, manufacturer_id, product_id, product_type, firmware_version_range, device_class_generic, device_class_specific, required_values, absent_values, allow_multi, assumed_state, entity_registry_enabled_default, entity_category) -> None: ...

DOOR_LOCK_CURRENT_MODE_SCHEMA: Incomplete
SWITCH_MULTILEVEL_CURRENT_VALUE_SCHEMA: Incomplete
SWITCH_MULTILEVEL_TARGET_VALUE_SCHEMA: Incomplete
SWITCH_BINARY_CURRENT_VALUE_SCHEMA: Incomplete
SIREN_TONE_SCHEMA: Incomplete
WINDOW_COVERING_COVER_CURRENT_VALUE_SCHEMA: Incomplete
WINDOW_COVERING_SLAT_CURRENT_VALUE_SCHEMA: Incomplete
DISCOVERY_SCHEMAS: Incomplete

def async_discover_node_values(node: ZwaveNode, device: DeviceEntry, discovered_value_ids: dict[str, set[str]]) -> Generator[ZwaveDiscoveryInfo, None, None]: ...
def async_discover_single_value(value: ZwaveValue, device: DeviceEntry, discovered_value_ids: dict[str, set[str]]) -> Generator[ZwaveDiscoveryInfo, None, None]: ...
def async_discover_single_configuration_value(value: ConfigurationValue) -> Generator[ZwaveDiscoveryInfo, None, None]: ...
def check_value(value: ZwaveValue, schema: ZWaveValueDiscoverySchema) -> bool: ...
def check_device_class(device_class: DeviceClassItem, required_value: set[str] | None) -> bool: ...

from .const import ENTITY_DESC_KEY_BATTERY as ENTITY_DESC_KEY_BATTERY, ENTITY_DESC_KEY_CO as ENTITY_DESC_KEY_CO, ENTITY_DESC_KEY_CO2 as ENTITY_DESC_KEY_CO2, ENTITY_DESC_KEY_CURRENT as ENTITY_DESC_KEY_CURRENT, ENTITY_DESC_KEY_ENERGY_MEASUREMENT as ENTITY_DESC_KEY_ENERGY_MEASUREMENT, ENTITY_DESC_KEY_ENERGY_TOTAL_INCREASING as ENTITY_DESC_KEY_ENERGY_TOTAL_INCREASING, ENTITY_DESC_KEY_HUMIDITY as ENTITY_DESC_KEY_HUMIDITY, ENTITY_DESC_KEY_ILLUMINANCE as ENTITY_DESC_KEY_ILLUMINANCE, ENTITY_DESC_KEY_MEASUREMENT as ENTITY_DESC_KEY_MEASUREMENT, ENTITY_DESC_KEY_POWER as ENTITY_DESC_KEY_POWER, ENTITY_DESC_KEY_POWER_FACTOR as ENTITY_DESC_KEY_POWER_FACTOR, ENTITY_DESC_KEY_PRESSURE as ENTITY_DESC_KEY_PRESSURE, ENTITY_DESC_KEY_SIGNAL_STRENGTH as ENTITY_DESC_KEY_SIGNAL_STRENGTH, ENTITY_DESC_KEY_TARGET_TEMPERATURE as ENTITY_DESC_KEY_TARGET_TEMPERATURE, ENTITY_DESC_KEY_TEMPERATURE as ENTITY_DESC_KEY_TEMPERATURE, ENTITY_DESC_KEY_TIMESTAMP as ENTITY_DESC_KEY_TIMESTAMP, ENTITY_DESC_KEY_TOTAL_INCREASING as ENTITY_DESC_KEY_TOTAL_INCREASING, ENTITY_DESC_KEY_VOLTAGE as ENTITY_DESC_KEY_VOLTAGE
from collections.abc import Iterable
from typing import Any
from zwave_js_server.const.command_class.meter import MeterScaleType as MeterScaleType
from zwave_js_server.const.command_class.multilevel_sensor import MultilevelSensorType
from zwave_js_server.model.node import Node as ZwaveNode
from zwave_js_server.model.value import Value as ZwaveValue

METER_DEVICE_CLASS_MAP: dict[str, set[MeterScaleType]]
MULTILEVEL_SENSOR_DEVICE_CLASS_MAP: dict[str, set[MultilevelSensorType]]

class ZwaveValueID:
    property_: Union[str, int]
    command_class: int
    endpoint: Union[int, None]
    property_key: Union[str, int, None]

class BaseDiscoverySchemaDataTemplate:
    static_data: Union[Any, None]
    def resolve_data(self, value: ZwaveValue) -> Any: ...
    def values_to_watch(self, resolved_data: Any) -> Iterable[ZwaveValue]: ...
    def value_ids_to_watch(self, resolved_data: Any) -> set[str]: ...
    @staticmethod
    def _get_value_from_id(node: ZwaveNode, value_id_obj: ZwaveValueID) -> Union[ZwaveValue, None]: ...

class DynamicCurrentTempClimateDataTemplate(BaseDiscoverySchemaDataTemplate):
    lookup_table: dict[Union[str, int], ZwaveValueID]
    dependent_value: Union[ZwaveValueID, None]
    def resolve_data(self, value: ZwaveValue) -> dict[str, Any]: ...
    def values_to_watch(self, resolved_data: dict[str, Any]) -> Iterable[ZwaveValue]: ...
    @staticmethod
    def current_temperature_value(resolved_data: dict[str, Any]) -> Union[ZwaveValue, None]: ...

class NumericSensorDataTemplate(BaseDiscoverySchemaDataTemplate):
    def resolve_data(self, value: ZwaveValue) -> Union[str, None]: ...

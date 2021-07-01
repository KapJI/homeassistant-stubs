from collections.abc import Iterable
from typing import Any
from zwave_js_server.model.node import Node as ZwaveNode
from zwave_js_server.model.value import Value as ZwaveValue

class ZwaveValueID:
    property_: Union[str, int]
    command_class: int
    endpoint: Union[int, None]
    property_key: Union[str, int, None]

class BaseDiscoverySchemaDataTemplate:
    def resolve_data(self, value: ZwaveValue) -> dict[str, Any]: ...
    def values_to_watch(self, resolved_data: dict[str, Any]) -> Iterable[ZwaveValue]: ...
    def value_ids_to_watch(self, resolved_data: dict[str, Any]) -> set[str]: ...
    @staticmethod
    def _get_value_from_id(node: ZwaveNode, value_id_obj: ZwaveValueID) -> Union[ZwaveValue, None]: ...

class DynamicCurrentTempClimateDataTemplate(BaseDiscoverySchemaDataTemplate):
    lookup_table: dict[Union[str, int], ZwaveValueID]
    dependent_value: ZwaveValueID
    def resolve_data(self, value: ZwaveValue) -> dict[str, Any]: ...
    def values_to_watch(self, resolved_data: dict[str, Any]) -> Iterable[ZwaveValue]: ...
    @staticmethod
    def current_temperature_value(resolved_data: dict[str, Any]) -> Union[ZwaveValue, None]: ...

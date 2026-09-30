import abc
import probatio
from .config_validation import BITMASK_SCHEMA as BITMASK_SCHEMA, COMMAND_CLASS_SCHEMA as COMMAND_CLASS_SCHEMA
from .const import ATTR_COMMAND_CLASS as ATTR_COMMAND_CLASS, ATTR_CONFIG_PARAMETER as ATTR_CONFIG_PARAMETER, ATTR_CONFIG_PARAMETER_BITMASK as ATTR_CONFIG_PARAMETER_BITMASK, ATTR_ENDPOINT as ATTR_ENDPOINT, ATTR_PROPERTY as ATTR_PROPERTY, ATTR_PROPERTY_KEY as ATTR_PROPERTY_KEY, ATTR_VALUE as ATTR_VALUE, NODE_STATUSES as NODE_STATUSES
from .helpers import async_bypass_dynamic_config_validation as async_bypass_dynamic_config_validation, async_get_node_from_device_id as async_get_node_from_device_id, get_zwave_value_from_config as get_zwave_value_from_config, node_status_matches as node_status_matches, value_matches_state as value_matches_state
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Iterable
from homeassistant.const import ATTR_DEVICE_ID as ATTR_DEVICE_ID, CONF_OPTIONS as CONF_OPTIONS
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.condition import ATTR_BEHAVIOR as ATTR_BEHAVIOR, BEHAVIOR_ALL as BEHAVIOR_ALL, BEHAVIOR_ANY as BEHAVIOR_ANY, Condition as Condition, ConditionCheckParams as ConditionCheckParams, ConditionConfig as ConditionConfig
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any, Unpack, override
from zwave_js_server.model.node import Node as ZwaveNode

CONF_STATUS: str
_CONDITION_VALUE_SCHEMA: Incomplete
_BASE_SCHEMA_DICT: dict[probatio.Marker, Any]
_NODE_STATUS_OPTIONS_SCHEMA_DICT: dict[probatio.Marker, Any]
_VALUE_OPTIONS_SCHEMA_DICT: dict[probatio.Marker, Any]
_CONFIG_PARAMETER_OPTIONS_SCHEMA_DICT: dict[probatio.Marker, Any]

def _condition_schema(options_schema_dict: dict[probatio.Marker, Any]) -> probatio.Schema: ...
@callback
def _async_resolve_nodes(hass: HomeAssistant, device_ids: Iterable[str]) -> set[ZwaveNode]: ...

class _ZwaveNodeCondition(Condition, metaclass=abc.ABCMeta):
    _schema: probatio.Schema
    @classmethod
    @override
    async def async_validate_config(cls, hass: HomeAssistant, config: ConfigType) -> ConfigType: ...
    @classmethod
    def _validate_nodes(cls, nodes: set[ZwaveNode], options: dict[str, Any]) -> None: ...
    _options: Incomplete
    def __init__(self, hass: HomeAssistant, config: ConditionConfig) -> None: ...
    @abc.abstractmethod
    def _node_matches(self, node: ZwaveNode) -> bool: ...
    @override
    def _async_check(self, **kwargs: Unpack[ConditionCheckParams]) -> bool: ...

class NodeStatusCondition(_ZwaveNodeCondition):
    _schema: Incomplete
    @override
    def _node_matches(self, node: ZwaveNode) -> bool: ...

class _ZwaveValueCondition(_ZwaveNodeCondition, metaclass=abc.ABCMeta):
    @classmethod
    @abc.abstractmethod
    def _value_config(cls, options: dict[str, Any]) -> dict[str, Any]: ...
    @classmethod
    @abc.abstractmethod
    def _value_description(cls, options: dict[str, Any]) -> str: ...
    @classmethod
    @override
    def _validate_nodes(cls, nodes: set[ZwaveNode], options: dict[str, Any]) -> None: ...
    @override
    def _node_matches(self, node: ZwaveNode) -> bool: ...

class ValueCondition(_ZwaveValueCondition):
    _schema: Incomplete
    @classmethod
    @override
    def _value_config(cls, options: dict[str, Any]) -> dict[str, Any]: ...
    @classmethod
    @override
    def _value_description(cls, options: dict[str, Any]) -> str: ...

class ConfigParameterCondition(_ZwaveValueCondition):
    _schema: Incomplete
    @classmethod
    @override
    def _value_config(cls, options: dict[str, Any]) -> dict[str, Any]: ...
    @classmethod
    @override
    def _value_description(cls, options: dict[str, Any]) -> str: ...

CONDITIONS: dict[str, type[Condition]]

async def async_get_conditions(hass: HomeAssistant) -> dict[str, type[Condition]]: ...

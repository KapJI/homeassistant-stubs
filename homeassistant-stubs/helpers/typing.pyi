from .deprecation import DeferredDeprecatedAlias as DeferredDeprecatedAlias, all_with_deprecated_constants as all_with_deprecated_constants, check_if_deprecated_constant as check_if_deprecated_constant, dir_with_deprecated_constants as dir_with_deprecated_constants
from _typeshed import Incomplete
from collections.abc import Mapping
from enum import Enum
from typing import Any, Never

GPSType = tuple[float, float]
ConfigType = dict[str, Any]
DiscoveryInfoType = dict[str, Any]
ServiceDataType = dict[str, Any]
StateType: Incomplete
TemplateVarsType: Incomplete
NoEventData = Mapping[str, Never]
VolSchemaType: Incomplete
VolDictType: Incomplete
QueryType = Any

class UndefinedType(Enum):
    _singleton: int

UNDEFINED: Incomplete

def _deprecated_typing_helper(attr: str) -> DeferredDeprecatedAlias: ...

_DEPRECATED_ContextType: Incomplete
_DEPRECATED_EventType: Incomplete
_DEPRECATED_HomeAssistantType: Incomplete
_DEPRECATED_ServiceCallType: Incomplete
__getattr__: Incomplete
__dir__: Incomplete
__all__: Incomplete

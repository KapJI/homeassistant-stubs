import homeassistant.core
from _typeshed import Incomplete
from collections.abc import Mapping
from enum import Enum
from typing import Any, Optional, Union

GPSType = tuple[float, float]
ConfigType = dict[str, Any]
ContextType = homeassistant.core.Context
DiscoveryInfoType = dict[str, Any]
EventType = homeassistant.core.Event
ServiceDataType = dict[str, Any]
StateType = Union[None, str, int, float]
TemplateVarsType = Optional[Mapping[str, Any]]
QueryType = Any

class UndefinedType(Enum):
    _singleton: int

UNDEFINED: Incomplete
HomeAssistantType = homeassistant.core.HomeAssistant
ServiceCallType = homeassistant.core.ServiceCall

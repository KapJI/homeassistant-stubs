import homeassistant.core
from _typeshed import Incomplete
from enum import Enum
from typing import Any

GPSType = tuple[float, float]
ConfigType = dict[str, Any]
ContextType = homeassistant.core.Context
DiscoveryInfoType = dict[str, Any]
EventType = homeassistant.core.Event
ServiceDataType = dict[str, Any]
StateType: Incomplete
TemplateVarsType: Incomplete
QueryType = Any

class UndefinedType(Enum):
    _singleton: int

UNDEFINED: Incomplete
HomeAssistantType = homeassistant.core.HomeAssistant
ServiceCallType = homeassistant.core.ServiceCall

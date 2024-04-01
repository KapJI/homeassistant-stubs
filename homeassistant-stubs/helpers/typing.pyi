import homeassistant
from _typeshed import Incomplete
from enum import Enum
from typing import Any, TypeVar

_DataT = TypeVar('_DataT')
GPSType = tuple[float, float]
ConfigType = dict[str, Any]
ContextType = homeassistant.core.Context
DiscoveryInfoType = dict[str, Any]
ServiceDataType = dict[str, Any]
StateType: Incomplete
TemplateVarsType: Incomplete
QueryType = Any

class UndefinedType(Enum):
    _singleton: int

UNDEFINED: Incomplete
EventType = homeassistant.core.Event
HomeAssistantType = homeassistant.core.HomeAssistant
ServiceCallType = homeassistant.core.ServiceCall
